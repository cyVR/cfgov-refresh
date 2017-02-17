from __future__ import absolute_import

import HTMLParser

from django.db import models
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.apps import apps
# from django.utils.html import strip_tags

# from django.utils.encoding import python_2_unicode_compatible
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
# from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from v1.util.migrations import get_or_create_page

SORT_ASPECTS = [
    ('most relevant', '-score'),
    ('most helpful', '-helpfulness_score'),
    ('most viewed', '-views'),
    ('recently updated', '-updated_at'),
]

YES = 'YES'
NO = 'NO'
QUESTIONRATING_CHOICES = (
    ('1', YES),
    ('0', NO)
)


class QuestionTopic(models.Model):
    name = models.CharField(max_length=255)
    name_es = models.CharField(max_length=255)
    slug = models.SlugField()
    slug_es = models.SlugField()
    intro = RichTextField()
    intro_es = RichTextField()
    panels = [
        FieldPanel('name'),
        FieldPanel('name_es'),
        FieldPanel('slug'),
        FieldPanel('slug_es'),
        FieldPanel('intro'),
        FieldPanel('intro_es'),
    ]

    def __str__(self):
        return self.name


class QuestionCategory(models.Model):
    name = models.CharField(max_length=255)
    name_es = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField()
    slug_es = models.SlugField(null=True, blank=True)
    featured = models.BooleanField(default=False)
    weight = models.IntegerField(default=1)
    description = RichTextField(blank=True)
    more_info = models.TextField(blank=True)
    # featured_questions = models.ManyToManyField(
    #     'Question', symmetrical=False, blank=True,)
    # parent = models.ForeignKey(
    #     'self',
    #     null=True,
    #     blank=True,
    #     limit_choices_to={'parent': None},
    #     default=None)
    # related_subcategories = models.ManyToManyField(
    #     'self',
    #     blank=True,
    #     default=None,
    # )

    panels = [
        FieldPanel('name'),
        FieldPanel('name_es'),
        FieldPanel('slug'),
        FieldPanel('slug_es'),
        FieldPanel('featured'),
        FieldPanel('weight'),
        FieldPanel('description'),
        FieldPanel('more_info'),
    ]

    # def get_smth(self):
    #     return self

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('kbsearch') + \
            "?selected_facets=category_exact:" + self.slug

    def get_babel_absolute_url(self):
        return reverse('babel_search') + \
            "?selected_facets=category_exact:" + self.slug_es

    def search_query(self):
        from haystack.query import SearchQuerySet
        sqs = SearchQuerySet()
        sqs = sqs.models(EnglishAnswer)
        sqs = sqs.filter(category=self.name)
        return sqs

    # def top_tags(self):
    #     sqs = self.search_query()
    #     sqs = sqs.facet('tag')
    #     return [pair[0] for pair
    #             in sqs.facet_counts()['fields']['tag']
    #             if pair[1] > 0]

    def get_babel_featured_answers(self):
        featured_questions = sorted(
            self.featured_questions.all(), key=lambda q: q.viewcount)[:2]
        featured_answers = SpanishAnswer.objects.filter(
            question__in=featured_questions)
        if len(featured_questions) < 2:
            featured_answers = SpanishAnswer.objects.filter(
                question__question_category=self
            ).order_by('-question__questioncounter')[:2]
        return featured_answers

    def get_english_featured_answers(self):
        featured_questions = sorted(
            self.featured_questions.all(), key=lambda q: q.viewcount)[:2]
        featured_answers = EnglishAnswer.objects.filter(
            question__in=featured_questions)
        if len(featured_questions) < 2:
            featured_answers = EnglishAnswer.objects.filter(
                question__question_category=self
            ).order_by('-question__questioncounter')[:2]
        return featured_answers

    class Meta:
        ordering = ["weight"]
        verbose_name_plural = "Question categories"


WORKFLOW_STATE = [
    ('SUBMITTED', 'Submitted'),
    ('REJECTED', 'Rejected'),
    ('DUPLICATE', 'Duplicate'),
    ('REVIEW', 'Review'),
    ('APPROVED', 'Approved'),
    ('DELETED', 'Deleted'),
    ('SPAM', 'Spam'),
]


class Question(models.Model):
    title = RichTextField()
    topic = models.ForeignKey(QuestionTopic, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(default=timezone.now)
    # question_category = models.ManyToManyField(QuestionCategory)
    # audiences = models.ManyToManyField('Audience', blank=True)
    # related_questions = models.ManyToManyField(
    #     'self', symmetrical=False, blank=True)

    class Meta:
        ordering = ['id']

    panels = [
        FieldPanel('title'),
        # FieldPanel('topic'),
        # FieldPanel('created_at'),
        # FieldPanel('updated_at'),
        # FieldPanel('publish_date'),
        # FieldPanel('audiences'),
        # FieldPanel('related_questions'),
    ]

    def __str__(self):
        return "{} {}".format(self.id, self.title)

    @property
    def counter(self):
        mycounter, created = QuestionCounter.objects.get_or_create(
            question=self)
        if created:
            mycounter.save()
        return mycounter

    def boost(self):
        return 1.0

    # def audience_strings(self):
    #     for audience in self.audiences.all():
    #         yield audience.name

    def viewcount(self):
        return self.counter.viewcount

    def get_rating_url(self):
        return reverse('rate_question', kwargs={'question_id': self.id})

    def helpfulness_score(self):
        return sum([r.value for r in self.questionrating_set.all()])

    def get_english_answer(self):
        try:
            return EnglishAnswer.objects.get(question=self)
        except ObjectDoesNotExist:
            return None

    def get_spanish_answer(self):
        try:
            return SpanishAnswer.objects.get(question=self)
        except ObjectDoesNotExist:
            return None

    def get_english_answer_state(self):
        try:
            return self.get_english_answer().workflow_state
        except AttributeError:
            return None

    def get_spanish_answer_state(self):
        try:
            return self.get_spanish_answer().workflow_state
        except AttributeError:
            return None


class Answer(models.Model):
    topic = models.ForeignKey(QuestionTopic, blank=True, null=True)
    question = RichTextField(blank=True)
    short_answer = RichTextField(blank=True)
    answer = RichTextField(blank=True)
    slug = models.SlugField(max_length=255, blank=True)
    question_es = RichTextField(blank=True)
    short_answer_es = RichTextField(blank=True)
    answer_es = RichTextField(blank=True)
    slug_es = models.SlugField(max_length=255, blank=True)

    def __str__(self):
        return "{} {}".format(self.id, self.question.encode('utf-8'))

    def create_page(self, parent):
        """Create an English Answer page"""
        # from ask_cfpb.models.pages import AnswerPage
        page = get_or_create_page(
            apps,
            'ask_cfpb',
            'AnswerPage',
            self.question,
            self.slug,
            parent,
            live=False,
            shared=True,
            answer_base=self,
            question=self.question,
            answer=self.answer,
            is_english=True,
            is_spanish=False,
            question_topic=self.topic,
            one_sentence_answer=self.short_answer)
        print "created page {}".format(page.url_path)

    def create_spanish_page(self, parent):
        """Create a Spanish Answer page"""
        # from ask_cfpb.models.pages import AnswerPage
        page = get_or_create_page(
            apps,
            'ask_cfpb',
            'AnswerPage',
            self.question_es,
            self.slug_es,
            parent,
            live=False,
            shared=True,
            answer_base=self,
            question=self.question_es,
            answer=self.answer_es,
            is_english=False,
            is_spanish=True,
            question_topic=self.topic,
            one_sentence_answer=self.short_answer_es)
        print "created page {}".format(page.url_path)

    def create_pages(self):
        parent_page = Page.objects.get(slug='ask-cfpb')
        if self.answer:
            self.create_page(parent_page)
        if self.answer_es:
            self.create_spanish_page(parent_page)


class AnswerBase(models.Model):
    question = models.OneToOneField(Question)
    title = RichTextField(blank=True)
    title_draft = RichTextField(blank=True)
    slug = models.SlugField(max_length=255, blank=True)
    answer = RichTextField(blank=True)
    answer_draft = RichTextField(blank=True)
    # tagging = models.CharField(max_length=1000, blank=True)
    # tagging_draft = models.CharField(max_length=1000, default='')

    panels = [
        # FieldPanel('question'),
        FieldPanel('title'),
        # FieldPanel('title_draft'),
        FieldPanel('slug'),
        FieldPanel('answer'),
        # FieldPanel('answer_draft'),
    ]

    class Meta:
        abstract = True
        ordering = ['question__id']

    def __str__(self):
        return "{} {}".format(self.question.id, self.title)

    def save(self, *args, **kwargs):
        super(Answer, self).save(*args, **kwargs)
        self.question.updated_at = timezone.now
        self.question.save()

    # def tags(self):
    #     for tag in self.tagging.split(','):
    #         tag = tag.replace('"', '')
    #         tag = tag.strip()
    #         if tag != u'':
    #             yield tag

    def titles(self):
        html_parser = HTMLParser.HTMLParser()
        unescaped = html_parser.unescape(self.title)
        return [unescaped]

    def parsed_answer(self):
        html_parser = HTMLParser.HTMLParser()
        unescaped = html_parser.unescape(self.answer)
        return unescaped

    # def get_open_graph_title(self):
    #     if self.open_graph_title:
    #         title = self.open_graph_title
    #     else:
    #         title = self.title

    #     return strip_tags(title)

    # def get_open_graph_description(self):
    #     if self.open_graph_description:
    #         description = self.open_graph_description
    #     else:
    #         description = self.answer[:500]

    #     return strip_tags(description)

    # def get_twitter_text(self):
    #     if self.twitter_text:
    #         text = self.twitter_text
    #     else:
    #         if len(self.title) <= 103:
    #             text = self.title
    #         else:
    #             truncated_title = self.title[:100]
    #             truncated_words = ' '.join(truncated_title.split(' ')[:-1])
    #             text = '%s...' % truncated_words

    #     return strip_tags(text)


class UpsellItem(models.Model):
    title = models.CharField(max_length=255)
    show_title = models.BooleanField(default=False)
    text = models.TextField()

    def __str__(self):
        return self.title


class EnglishAnswer(AnswerBase):
    workflow_state = models.CharField(
        'english workflow state',
        max_length=255,
        choices=WORKFLOW_STATE,
        default='SUBMITTED')
    upsellitem = models.ForeignKey(
        UpsellItem,
        related_name='upsellitem',
        blank=True,
        null=True)
    one_sentence_answer = RichTextField(blank=True)
    one_sentence_answer_draft = RichTextField(blank=True)

    panels = [
        # FieldPanel('question'),
        FieldPanel('title'),
        # FieldPanel('title_draft'),
        FieldPanel('slug'),
        FieldPanel('answer'),
        # FieldPanel('answer_draft'),
        FieldPanel('workflow_state'),
        FieldPanel('upsellitem'),
        FieldPanel('one_sentence_answer'),
        # FieldPanel('one_sentence_answer_draft'),
    ]

    # def catname(self):
    #     return [cat.slug for cat in self.question.question_category.all()]

    def get_absolute_url(self):
        return reverse(
            'view_question',
            kwargs={'question_id': self.question.id, 'slug': self.slug})

    def get_print_url(self):
        return reverse(
            'print_question',
            kwargs={'question_id': self.question.id, 'slug': self.slug})

    def get_related_answers(self):
        return EnglishAnswer.objects.filter(
            question__in=self.question.related_questions.all())

    def __str__(self):
        return self.title


class SpanishAnswer(AnswerBase):
    workflow_state = models.CharField(
        'spanish workflow state',
        max_length=255,
        choices=WORKFLOW_STATE,
        default='SUBMITTED')
    subtitle = None

    panels = [
        # FieldPanel('question'),
        FieldPanel('title'),
        # FieldPanel('title_draft'),
        FieldPanel('slug'),
        FieldPanel('answer'),
        # FieldPanel('answer_draft'),
        FieldPanel('workflow_state'),
    ]

    def get_absolute_url(self):
        return reverse(
            'babel_view_question',
            kwargs={'question_id': self.question.id,
                    'slug': self.slug,
                    'cat_slug': self.babel_first_category()})

    def get_print_url(self):
        return reverse(
            'babel_print_question',
            kwargs={'question_id': self.question.id,
                    'slug': self.slug,
                    'cat_slug': self.babel_first_category()})

    def get_rating_url(self):
        return reverse(
            'babel_rate_question',
            kwargs={'question_id': self.question.id})

    def babel_first_category(self):
        return self.question.question_category.all()[0].slug_es

    def get_related_answers(self):
        return SpanishAnswer.objects\
            .filter(question__in=self.question.related_questions.all())

    def __str__(self):
        return self.title.encode('utf-8')


class QuestionCounter(models.Model):
    question = models.ForeignKey(Question)
    viewcount = models.IntegerField(default=0)


# class Audience(models.Model):
#     name = models.CharField(max_length=255)

#     panels = [
#         FieldPanel('name'),
#     ]

#     def __str__(self):
#         return self.name


class RatingAdjective(models.Model):
    word = models.CharField(max_length=255)
    word_es = models.CharField(max_length=255, null=True, blank=True)
    value = models.IntegerField(default=0)
    followup_question = models.TextField(blank=True)

    def __str__(self):
        return self.word


class QuestionRating(models.Model):
    question = models.ForeignKey(Question)
    adjective = models.ForeignKey(RatingAdjective)
    helpful = models.CharField(
        max_length=1,
        choices=QUESTIONRATING_CHOICES,
        null=True)
    looking_for = models.TextField(null=True)
    followup_answer = models.TextField(blank=True)
    value = models.IntegerField(default=0)
    submitted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "%s" % (self.adjective)


class BabelQuestionRating(models.Model):
    question = models.ForeignKey(Question)
    adjectives = models.ManyToManyField(RatingAdjective)
    followup_answer = models.TextField(blank=True)
    value = models.IntegerField(default=0)
    submitted = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'spanish question rating'

    def get_adjectives(self):
        return "\n".join([s.word for s in self.adjectives.all()])


class QuestionSubmission(models.Model):
    question = models.TextField()
    comment = models.TextField(blank=True)
    searchterms = models.CharField(blank=True, max_length=2000)
    email = models.EmailField(blank=True)
    workflow_state = models.CharField(
        max_length=255, choices=WORKFLOW_STATE, default='SUBMITTED')
    submitted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.question


# class RelatedTermSet(models.Model):
#     name = models.CharField(
#         max_length=255,
#         help_text="A label for this set of terms.")
#     terms = models.TextField(help_text=("Terms that should be treated "
#                                         "as synonyms. Put each term "
#                                         "on its own line."))

#     def __str__(self):
#         return self.name

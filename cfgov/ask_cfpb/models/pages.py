from __future__ import absolute_import

from django.utils import timezone
from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    ObjectList,
    TabbedInterface)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import PageManager

from v1.models import CFGOVPage

from ask_cfpb.models.django import QuestionTopic, Answer


class AnswerPage(CFGOVPage):
    """
    Page type for Ask CFPB answers.
    """
    question = RichTextField(blank=True)
    answer = RichTextField(blank=True)
    one_sentence_answer = RichTextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(default=timezone.now)
    question_topic = models.ForeignKey(
        QuestionTopic,
        blank=True,
        null=True,
        related_name='+',
        on_delete=models.PROTECT)
    answer_base = models.ForeignKey(
        Answer,
        blank=True,
        null=True,
        # related_name='+',
        on_delete=models.PROTECT)
    is_english = models.BooleanField()
    is_spanish = models.BooleanField()

    content_panels = CFGOVPage.content_panels + [
        FieldPanel('question'),
        FieldPanel('one_sentence_answer', classname="full"),
        FieldPanel('answer', classname="full"),
        FieldPanel('is_english'),
        FieldPanel('is_spanish'),
        FieldPanel('question_topic'),
        FieldPanel('answer_base'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(CFGOVPage.settings_panels, heading='Configuration'),
    ])

    template = 'ask-answer-page/index.html'
    objects = PageManager()

import datetime

from django.template.defaultfilters import slugify

from ask_cfpb.models import Answer, QuestionTopic
from knowledgebase.models import Question


def get_en_answer(ID, topic, en_answer):
    answer, created = Answer.objects.get_or_create(
        id=ID,
        topic=topic,
        slug=en_answer.slug,
        question=en_answer.title)
    return answer


def get_es_answer(ID, topic, es_answer):
    answer, created = Answer.objects.get_or_create(
        id=ID,
        topic=topic,
        slug_es=es_answer.slug,
        question_es=es_answer.title)
    return answer


def fill_out_es_answer(answer, es_answer):
    answer.slug_es = es_answer.slug
    answer.question_es = es_answer.title
    answer.answer_es = es_answer.answer
    answer.short_answer_es = u''
    return answer


def build_answer(ID, topic, question, en_answer=None, es_answer=None):
    if en_answer:
        answer_base = get_en_answer(ID, topic, en_answer)
        answer_base.answer = en_answer.answer
        answer_base.short_answer = en_answer.one_sentence_answer
        if es_answer:
            answer_base = fill_out_es_answer(answer_base, es_answer)
    elif es_answer:  # no English answer to be had
        answer_base = get_es_answer(ID, topic, es_answer)
        answer_base = fill_out_es_answer(answer_base, es_answer)
    else:  # no answers formulated yet!
        print ("Creating an Answer object "
               "with a question but no answers: {}".format(question))
        answer_base, created = Answer.objects.get_or_create(
            id=ID,
            topic=topic,
            slug=slugify(datetime.datetime.now()),
            question=question)

    return answer_base


def migrate_answer(question):
    parent_category = question.question_category.filter(parent=None).first()
    topic = QuestionTopic.objects.get(slug=parent_category.slug)
    answer = build_answer(
        question.id,
        topic,
        question.title,
        question.get_english_answer(),
        question.get_spanish_answer())
    if answer:
        answer.save()
        # print "saved answer object {}".format(answer.slug)


def migrate(queryset):
    counter = 0
    for question in queryset:
        counter += 1
        if counter % 100 == 0:
            print "{}\n".format(counter)
        migrate_answer(question)
    print "Migrated or updated {} answers.".format(counter)

if __name__ == "__main__":
    migrate(Question.objects.all())

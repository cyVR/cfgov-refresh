from ask_cfpb.models import Answer, QuestionTopic, NextStep
from ask_cfpb.models import Audience as ASK_audience
from ask_cfpb.models import QuestionCategory as ASK_QC
from knowledgebase.models import QuestionCategory as QC
from knowledgebase.models import Question, Audience, UpsellItem, EnglishAnswer


def migrate_topics():
    topics = QC.objects.filter(parent=None)
    create_count = 0
    update_count = 0
    for qc in topics:
        qt, cr = QuestionTopic.objects.get_or_create(
            slug=qc.slug,
            slug_es=qc.slug_es,
            name=qc.name,
            name_es=qc.name_es,
            intro=qc.description,
            intro_es='')
        if cr:
            create_count += 1
        else:
            update_count += 1
    print("Found {} topic categories, "
          "created {} "
          "and updated {}".format(
              topics.count(), create_count, update_count))


def get_en_answer(ID, topic, en_answer):
    answer, created = Answer.objects.get_or_create(
        id=ID,
        topic=topic,
        slug=en_answer.slug)
    answer.question = en_answer.title
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
    answer.workflow_state_es = es_answer.workflow_state
    return answer


def build_answer(question, topic, en_answer=None, es_answer=None):
    if en_answer:
        answer_base = get_en_answer(question.id, topic, en_answer)
        answer_base.answer = en_answer.answer
        answer_base.workflow_state = en_answer.workflow_state
        answer_base.created_at = question.created_at
        answer_base.updated_at = question.updated_at
        answer_base.short_answer = en_answer.one_sentence_answer
        for qc in question.question_category.exclude(parent=None):
            answer_base.question_category.add(ASK_QC.objects.get(slug=qc.slug))
        if es_answer:
            answer_base = fill_out_es_answer(answer_base, es_answer)
    elif es_answer:  # no English answer to be had
        answer_base = get_es_answer(question.id, topic, es_answer)
        answer_base = fill_out_es_answer(answer_base, es_answer)
    else:  # no answers for this question yet, so we'll save with an ID slug
        answer_base, created = Answer.objects.get_or_create(
            id=question.id,
            topic=topic,
            slug="answer-{}".format(question.id))
    return answer_base


def migrate_answer(question):
    parent_category = question.question_category.filter(parent=None).first()
    topic = QuestionTopic.objects.get(slug=parent_category.slug)
    answer = build_answer(
        question,
        topic,
        question.get_english_answer(),
        question.get_spanish_answer())
    if answer:
        answer.save()


def migrate_questions():
    queryset = Question.objects.all()
    print("Migrating {} KB questions ...".format(queryset.count()))
    counter = 0
    for question in queryset:
        counter += 1
        if counter % 100 == 0:
            print "{}".format(counter)
        migrate_answer(question)
    print "Migrated or updated {} answers.".format(counter)


def migrate_audiences():
    audiences_created = 0
    audience_relation_count = 0
    for audience in Audience.objects.all():
        new_audience, cr = ASK_audience.objects.get_or_create(
            id=audience.id,
            name=audience.name)
        if cr:
            audiences_created += 1
    for question in Question.objects.all():
        ask_cfpb_answer = Answer.objects.get(id=question.id)
        for audience in question.audiences.all():
            ask_cfpb_answer.audiences.add(
                ASK_audience.objects.get(id=audience.id))
            audience_relation_count += 1
    print("Found {} Audience objects; needed to migrate {}\n"
          "Created {} Audience links".format(
              Audience.objects.count(),
              audiences_created,
              audience_relation_count))


def migrate_next_steps():
    """Move knowledgebase UpsellItems to ask_cfpb NextSteps"""
    upsells_created = 0
    upsells_updated = 0
    nextsteps_linked = 0
    upsells = UpsellItem.objects.all()
    print("Migrating {} UpsellItems to the NextStep model ...".format(
        upsells.count()))
    for upsell in upsells:
        nextstep, cr = NextStep.objects.get_or_create(
            id=upsell.id,
            title=upsell.title)
        nextstep.show_title = upsell.show_title
        nextstep.text = upsell.text
        nextstep.save()
        if cr:
            upsells_created += 1
        else:
            upsells_updated += 1
    print("created {} NextStep objects "
          "and updated {}".format(upsells_created, upsells_updated))
    for ea in EnglishAnswer.objects.all():
        if ea.upsellitem:
            answer = Answer.objects.get(id=ea.question.id)
            answer.next_step = NextStep.objects.get(id=ea.upsellitem.id)
            answer.save()
            nextsteps_linked += 1
    print("Created {} NextStep links\n".format(nextsteps_linked))


def migrate_categories():
    categories = QC.objects.exclude(parent=None)
    create_count = 0
    update_count = 0
    for qc in categories:
        cat, cr = ASK_QC.objects.get_or_create(
            id=qc.id,
            name=qc.name,
            name_es=qc.name_es,
            slug=qc.slug,
            slug_es=qc.slug_es)
        cat.featured = qc.featured
        cat.weight = qc.weight
        cat.description = qc.description
        cat.more_info = qc.more_info
        cat.parent = QuestionTopic.objects.get(slug=qc.parent.slug)
        cat.save()
        if cr:
            create_count += 1
        else:
            update_count += 1
    print("created {} ASK categories "
          "and updated {}".format(create_count, update_count))


def add_related_categories():
    update_count = 0
    for cat in QC.objects.exclude(parent=None):
        ask_qc = ASK_QC.objects.get(id=cat.id)
        for related in cat.related_subcategories.exclude(parent=None):
            ask_qc.related_categories.add(ASK_QC.objects.get(id=related.id))
        ask_qc.save()
        update_count += 1
    print("updated related categories for {} ASK categories.").format(
        update_count)


def add_featured_questions():
    update_count = 0
    for cat in QC.objects.exclude(parent=None):
        ask_qc = ASK_QC.objects.get(id=cat.id)
        for featured in cat.featured_questions.all():
            ask_qc.featured_questions.add(Answer.objects.get(id=featured.id))
        ask_qc.save()
        update_count += 1
    print("updated featured questions for {} ASK categories.").format(
        update_count)


def migrate_knowledgebase():
    migrate_topics()
    migrate_categories()
    add_related_categories()
    migrate_questions()
    add_featured_questions()
    migrate_audiences()
    migrate_next_steps()

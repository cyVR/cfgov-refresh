from knowledgebase.models import QuestionCategory as QC
from ask_cfpb.models import QuestionTopic as QT


def migrate_topics():
    topics = QC.objects.filter(parent=None)
    create_count = 0
    for qc in topics:
        qt, cr = QT.objects.get_or_create(
            slug=qc.slug,
            slug_es=qc.slug_es,
            name=qc.name,
            name_es=qc.name_es,
            intro=qc.description,
            intro_es='')
        if cr:
            create_count += 1
        print "Found {} topic categories and created {}".format(
            topics.count(), create_count)

if __name__ == "__main__":
    migrate_topics()

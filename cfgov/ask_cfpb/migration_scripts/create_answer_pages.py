from ask_cfpb.models import Answer


def create_answer_pages(queryset, approve_all=False):
    if queryset:
        for each in queryset:
            each.create_pages(approve_all=approve_all)
    else:
        print "No Answer objects found in queryset."


def update_all(approve_all=False):
    create_answer_pages(Answer.objects.all(), approve_all=approve_all)

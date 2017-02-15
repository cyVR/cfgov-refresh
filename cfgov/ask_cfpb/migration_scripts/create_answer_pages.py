from ask_cfpb.models import Answer


def create_answer_pages(queryset):
    if queryset:
        for each in queryset:
            each.create_pages()
    else:
        print "No Answer objects found in queryset."

if __name__ == "__main__":

    create_answer_pages(Answer.objects.all())

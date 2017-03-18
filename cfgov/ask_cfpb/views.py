from django.shortcuts import get_object_or_404, redirect

from .models.pages import AnswerPage


def view_answer(request, slug, language, answer_id):
    answer_page = get_object_or_404(
        AnswerPage, language=language, answer_base__id=answer_id)
    if answer_page.redirect_id:
        new_page = get_object_or_404(
            AnswerPage,
            language=language,
            answer_base__id=answer_page.redirect_id)
        return redirect(new_page.url)
    if "{}-{}-{}".format(slug, language, answer_id) != answer_page.slug:
        return redirect(answer_page.url)
    else:
        return answer_page.serve(request)

# from django.forms.models import ModelForm
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
# from wagtail.contrib.modeladmin.views import (
#     CreateView, EditView, InspectView)

from ask_cfpb.models import (
    # Question,
    QuestionCategory,
    QuestionTopic,
    Answer,
    Audience,
    NextStep,
)


class NextStepModelAdmin(ModelAdmin):
    model = NextStep
    menu_label = 'Next steps'


class AudienceModelAdmin(ModelAdmin):
    model = Audience
    menu_label = 'Audiences'


class QuestionTopicAdmin(ModelAdmin):
    model = QuestionTopic
    menu_label = 'Question Topics'
    list_display = (
        'name', 'name_es', 'intro', 'intro_es')


class QuestionCategoryModelAdmin(ModelAdmin):
    model = QuestionCategory
    menu_label = 'Categories'
    list_display = (
        'name', 'weight', 'parent'
    )
    search_fields = (
        'name', 'weight')
    list_filter = ('parent', 'featured')


class AnswerModelAdmin(ModelAdmin):
    model = Answer
    menu_label = 'Answers'
    list_display = (
        'id', 'question', 'question_es', 'topic', 'updated_at', 'created_at')
    search_fields = (
        'id', 'question', 'question_es', 'answer', 'answer_es')
    list_filter = ('topic',)


# class EnglishAnswerModelAdmin(ModelAdmin):
#     model = EnglishAnswer
#     menu_label = 'Original English Answers'
    # create_view_class = JobCategoryCreateView
    # edit_view_class = JobCategoryEditView
    # inspect_view_class = JobCategoryInspectView


# class SpanishAnswerModelAdmin(ModelAdmin):
#     model = SpanishAnswer
#     menu_label = 'Original Spanish Answers'
    # create_view_class = JobCategoryCreateView
    # edit_view_class = JobCategoryEditView
    # inspect_view_class = JobCategoryInspectView


# class JobCategoryForm(ModelForm):
#     class Meta:
#         fields = '__all__'
#         model = JobCategory
#         widgets = {
#             'blurb': TinyMCE(attrs={'cols': 80, 'rows': 15}),
#         }


# class JobCategoryModelFormMixin(object):
#     def get_form_class(self):
#         return JobCategoryForm


# class JobCategoryCreateView(JobCategoryModelFormMixin, CreateView):
#     pass


# class JobCategoryEditView(JobCategoryModelFormMixin, EditView):
#     pass


# class JobCategoryInspectView(JobCategoryModelFormMixin, InspectView):
#     pass


# class JobRegionModelAdmin(ModelAdmin):
#     model = JobRegion
#     menu_label = 'Regions'
#     menu_icon = 'site'
#     list_display = ('abbreviation', 'name')


@modeladmin_register
class MyModelAdminGroup(ModelAdminGroup):
    menu_label = 'Ask CFPB'
    menu_icon = 'folder-open-inverse'
    items = (
        AudienceModelAdmin,
        QuestionTopicAdmin,
        QuestionCategoryModelAdmin,
        AnswerModelAdmin,
        NextStepModelAdmin,
        # SpanishAnswerModelAdmin,
    )

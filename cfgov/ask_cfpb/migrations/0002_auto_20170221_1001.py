# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_cfpb', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UpsellItem',
            new_name='NextStep',
        ),
        migrations.RemoveField(
            model_name='babelquestionrating',
            name='adjectives',
        ),
        migrations.RemoveField(
            model_name='babelquestionrating',
            name='question',
        ),
        migrations.RemoveField(
            model_name='englishanswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='englishanswer',
            name='upsellitem',
        ),
        migrations.RemoveField(
            model_name='question',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='questioncounter',
            name='question',
        ),
        migrations.RemoveField(
            model_name='questionrating',
            name='adjective',
        ),
        migrations.RemoveField(
            model_name='questionrating',
            name='question',
        ),
        migrations.DeleteModel(
            name='QuestionSubmission',
        ),
        migrations.RemoveField(
            model_name='spanishanswer',
            name='question',
        ),
        migrations.AddField(
            model_name='answer',
            name='next_step',
            field=models.ForeignKey(related_name='upsellitem', blank=True, to='ask_cfpb.NextStep', null=True),
        ),
        migrations.AddField(
            model_name='questioncategory',
            name='featured_questions',
            field=models.ManyToManyField(to='ask_cfpb.Answer', blank=True),
        ),
        migrations.AddField(
            model_name='questioncategory',
            name='parent',
            field=models.ForeignKey(default=None, blank=True, to='ask_cfpb.QuestionTopic', null=True),
        ),
        migrations.AddField(
            model_name='questioncategory',
            name='related_categories',
            field=models.ManyToManyField(default=None, related_name='_questioncategory_related_categories_+', null=True, to='ask_cfpb.QuestionCategory', blank=True),
        ),
        migrations.DeleteModel(
            name='BabelQuestionRating',
        ),
        migrations.DeleteModel(
            name='EnglishAnswer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='QuestionCounter',
        ),
        migrations.DeleteModel(
            name='QuestionRating',
        ),
        migrations.DeleteModel(
            name='RatingAdjective',
        ),
        migrations.DeleteModel(
            name='SpanishAnswer',
        ),
    ]

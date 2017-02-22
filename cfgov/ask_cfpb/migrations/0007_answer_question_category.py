# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_cfpb', '0006_answer_workflow_state_es'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question_category',
            field=models.ManyToManyField(to='ask_cfpb.QuestionCategory', blank=True),
        ),
    ]

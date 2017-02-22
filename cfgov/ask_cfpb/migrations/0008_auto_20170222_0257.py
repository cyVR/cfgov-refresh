# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ask_cfpb', '0007_answer_question_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questioncategory',
            options={'ordering': ['-weight'], 'verbose_name_plural': 'Question categories'},
        ),
        migrations.AlterField(
            model_name='answerpage',
            name='answer_base',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, blank=True, to='ask_cfpb.Answer', null=True),
        ),
        migrations.AlterField(
            model_name='questiontopic',
            name='intro',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='questiontopic',
            name='intro_es',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]

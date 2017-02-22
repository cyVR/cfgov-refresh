# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_cfpb', '0002_auto_20170221_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questioncategory',
            name='related_categories',
            field=models.ManyToManyField(default=None, related_name='_questioncategory_related_categories_+', to='ask_cfpb.QuestionCategory', blank=True),
        ),
    ]

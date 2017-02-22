# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_cfpb', '0008_auto_20170222_0257'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questiontopic',
            options={'ordering': ['name']},
        ),
    ]

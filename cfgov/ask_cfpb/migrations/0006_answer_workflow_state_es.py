# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_cfpb', '0005_auto_20170221_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='workflow_state_es',
            field=models.CharField(default='SUBMITTED', max_length=255, choices=[('SUBMITTED', 'Submitted'), ('REJECTED', 'Rejected'), ('APPROVED', 'Approved')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ask_cfpb', '0003_auto_20170221_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 0, 5, 27, 716751, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='tagging',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 0, 6, 40, 286239, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='workflow_state',
            field=models.CharField(default='SUBMITTED', max_length=255, choices=[('SUBMITTED', 'Submitted'), ('REJECTED', 'Rejected'), ('APPROVED', 'Approved')]),
        ),
        migrations.AddField(
            model_name='questiontopic',
            name='featured_questions',
            field=models.ManyToManyField(to='ask_cfpb.Answer', blank=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='audiences',
            field=models.ManyToManyField(to='ask_cfpb.Audience', blank=True),
        ),
    ]

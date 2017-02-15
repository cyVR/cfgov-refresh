# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0054_new_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('answer', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('short_answer', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('slug', models.SlugField(max_length=255, blank=True)),
                ('question_es', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('answer_es', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('short_answer_es', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('slug_es', models.SlugField(max_length=255, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerPage',
            fields=[
                ('cfgovpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='v1.CFGOVPage')),
                ('question', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('answer', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('one_sentence_answer', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_english', models.BooleanField()),
                ('is_spanish', models.BooleanField()),
                ('answer_base', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='ask_cfpb.Answer', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('v1.cfgovpage',),
        ),
        migrations.CreateModel(
            name='BabelQuestionRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('followup_answer', models.TextField(blank=True)),
                ('value', models.IntegerField(default=0)),
                ('submitted', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'spanish question rating',
            },
        ),
        migrations.CreateModel(
            name='EnglishAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('title_draft', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('slug', models.SlugField(max_length=255, blank=True)),
                ('answer', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('answer_draft', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('workflow_state', models.CharField(default=b'SUBMITTED', max_length=255, verbose_name=b'english workflow state', choices=[(b'SUBMITTED', b'Submitted'), (b'REJECTED', b'Rejected'), (b'DUPLICATE', b'Duplicate'), (b'REVIEW', b'Review'), (b'APPROVED', b'Approved'), (b'DELETED', b'Deleted'), (b'SPAM', b'Spam')])),
                ('one_sentence_answer', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('one_sentence_answer_draft', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'ordering': ['question__id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', wagtail.wagtailcore.fields.RichTextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='QuestionCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('name_es', models.CharField(max_length=255, null=True, blank=True)),
                ('slug', models.SlugField()),
                ('slug_es', models.SlugField(null=True, blank=True)),
                ('featured', models.BooleanField(default=False)),
                ('weight', models.IntegerField(default=1)),
                ('description', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('more_info', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['weight'],
                'verbose_name_plural': 'Question categories',
            },
        ),
        migrations.CreateModel(
            name='QuestionCounter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('viewcount', models.IntegerField(default=0)),
                ('question', models.ForeignKey(to='ask_cfpb.Question')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('helpful', models.CharField(max_length=1, null=True, choices=[(b'1', b'YES'), (b'0', b'NO')])),
                ('looking_for', models.TextField(null=True)),
                ('followup_answer', models.TextField(blank=True)),
                ('value', models.IntegerField(default=0)),
                ('submitted', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionSubmission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField()),
                ('comment', models.TextField(blank=True)),
                ('searchterms', models.CharField(max_length=2000, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('workflow_state', models.CharField(default=b'SUBMITTED', max_length=255, choices=[(b'SUBMITTED', b'Submitted'), (b'REJECTED', b'Rejected'), (b'DUPLICATE', b'Duplicate'), (b'REVIEW', b'Review'), (b'APPROVED', b'Approved'), (b'DELETED', b'Deleted'), (b'SPAM', b'Spam')])),
                ('submitted', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionTopic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('name_es', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('slug_es', models.SlugField()),
                ('intro', wagtail.wagtailcore.fields.RichTextField()),
                ('intro_es', wagtail.wagtailcore.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='RatingAdjective',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=255)),
                ('word_es', models.CharField(max_length=255, null=True, blank=True)),
                ('value', models.IntegerField(default=0)),
                ('followup_question', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpanishAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('title_draft', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('slug', models.SlugField(max_length=255, blank=True)),
                ('answer', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('answer_draft', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('workflow_state', models.CharField(default=b'SUBMITTED', max_length=255, verbose_name=b'spanish workflow state', choices=[(b'SUBMITTED', b'Submitted'), (b'REJECTED', b'Rejected'), (b'DUPLICATE', b'Duplicate'), (b'REVIEW', b'Review'), (b'APPROVED', b'Approved'), (b'DELETED', b'Deleted'), (b'SPAM', b'Spam')])),
                ('question', models.OneToOneField(to='ask_cfpb.Question')),
            ],
            options={
                'ordering': ['question__id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UpsellItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('show_title', models.BooleanField(default=False)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='questionrating',
            name='adjective',
            field=models.ForeignKey(to='ask_cfpb.RatingAdjective'),
        ),
        migrations.AddField(
            model_name='questionrating',
            name='question',
            field=models.ForeignKey(to='ask_cfpb.Question'),
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(blank=True, to='ask_cfpb.QuestionTopic', null=True),
        ),
        migrations.AddField(
            model_name='englishanswer',
            name='question',
            field=models.OneToOneField(to='ask_cfpb.Question'),
        ),
        migrations.AddField(
            model_name='englishanswer',
            name='upsellitem',
            field=models.ForeignKey(related_name='upsellitem', blank=True, to='ask_cfpb.UpsellItem', null=True),
        ),
        migrations.AddField(
            model_name='babelquestionrating',
            name='adjectives',
            field=models.ManyToManyField(to='ask_cfpb.RatingAdjective'),
        ),
        migrations.AddField(
            model_name='babelquestionrating',
            name='question',
            field=models.ForeignKey(to='ask_cfpb.Question'),
        ),
        migrations.AddField(
            model_name='answerpage',
            name='question_topic',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, blank=True, to='ask_cfpb.QuestionTopic', null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='topic',
            field=models.ForeignKey(blank=True, to='ask_cfpb.QuestionTopic', null=True),
        ),
    ]

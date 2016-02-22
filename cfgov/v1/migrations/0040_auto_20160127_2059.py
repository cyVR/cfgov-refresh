# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailsnippets.blocks
import v1.models.snippets
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0039_remove_blog_from_category_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browsefilterablepage',
            name='header',
            field=wagtail.wagtailcore.fields.StreamField([(b'text_introduction', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'intro', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])), (b'featured_content', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'category', wagtail.wagtailcore.blocks.ChoiceBlock(required=False, choices=[(b'featured-event', b'Featured event'), (b'featured-blog', b'Featured blog'), (b'featured-video', b'Featured video'), (b'featured-tool', b'Featured tool'), (b'featured-news', b'Featured news'), (b'featured', b'Featured')])), (b'post', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'show_post_link', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Render post link?')), (b'post_link_text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), label=b'Additional Links'))]))]),
        ),
        migrations.AlterField(
            model_name='browsepage',
            name='header',
            field=wagtail.wagtailcore.fields.StreamField([(b'text_introduction', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'intro', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])), (b'featured_content', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'category', wagtail.wagtailcore.blocks.ChoiceBlock(required=False, choices=[(b'featured-event', b'Featured event'), (b'featured-blog', b'Featured blog'), (b'featured-video', b'Featured video'), (b'featured-tool', b'Featured tool'), (b'featured-news', b'Featured news'), (b'featured', b'Featured')])), (b'post', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'show_post_link', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Render post link?')), (b'post_link_text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), label=b'Additional Links'))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='demopage',
            name='molecules',
            field=wagtail.wagtailcore.fields.StreamField([(b'number', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False))])), (b'half_width_link_blob', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))])), (b'text_introduction', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'intro', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])), (b'image_text_2575', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])), (b'image_text_5050', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False, blank=True)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'is_widescreen', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Use 16:9 image')), (b'is_button', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Show links as button')), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))])), (b'hero', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'background_color', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Use Hexcode colors e.g #F0F8FF', max_length=100, required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]))), (b'is_button', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])), (b'formfield_with_button', wagtail.wagtailcore.blocks.StructBlock([(b'btn_text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'required', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'id', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Type of form i.e emailForm, submission-form. Should be unique if multiple forms are used', max_length=100, required=False)), (b'info', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Disclaimer')), (b'label', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'type', wagtail.wagtailcore.blocks.ChoiceBlock(required=False, choices=[(b'text', b'Text'), (b'checkbox', b'Checkbox'), (b'email', b'Email'), (b'number', b'Number'), (b'url', b'URL'), (b'radio', b'Radio')])), (b'placeholder', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False))])), (b'call_to_action', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]))])), (b'expandable', wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'is_bordered', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_midtone', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_expanded', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'content', wagtail.wagtailcore.blocks.StreamBlock([(b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'email', wagtail.wagtailcore.blocks.StructBlock([(b'emails', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'phone', wagtail.wagtailcore.blocks.StructBlock([(b'fax', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False, label=b'Is this number a fax?')), (b'phones', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'number', wagtail.wagtailcore.blocks.CharBlock(max_length=15)), (b'vanity', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False)), (b'tty', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False))])))])), (b'address', wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=False)), (b'title', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'street', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'city', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=False)), (b'state', wagtail.wagtailcore.blocks.CharBlock(max_length=25, required=False)), (b'zip_code', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False))]))], blank=True))])), (b'featured_content', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'category', wagtail.wagtailcore.blocks.ChoiceBlock(required=False, choices=[(b'featured-event', b'Featured event'), (b'featured-blog', b'Featured blog'), (b'featured-video', b'Featured video'), (b'featured-tool', b'Featured tool'), (b'featured-news', b'Featured news'), (b'featured', b'Featured')])), (b'post', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'show_post_link', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Render post link?')), (b'post_link_text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), label=b'Additional Links'))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='sublandingpage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField([(b'text_introduction', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'intro', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])), (b'featured_content', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'category', wagtail.wagtailcore.blocks.ChoiceBlock(required=False, choices=[(b'featured-event', b'Featured event'), (b'featured-blog', b'Featured blog'), (b'featured-video', b'Featured video'), (b'featured-tool', b'Featured tool'), (b'featured-news', b'Featured news'), (b'featured', b'Featured')])), (b'post', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'show_post_link', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Render post link?')), (b'post_link_text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), label=b'Additional Links'))])), (b'image_text_25_75_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, icon=b'title')), (b'image_texts', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])))])), (b'image_text_50_50_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, icon=b'title')), (b'image_texts', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False, blank=True)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'is_widescreen', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Use 16:9 image')), (b'is_button', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Show links as button')), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))])))])), (b'full_width_text', wagtail.wagtailcore.blocks.StreamBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'edit')), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'body', wagtail.wagtailcore.blocks.TextBlock()), (b'citation', wagtail.wagtailcore.blocks.TextBlock())])), (b'cta', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]))])), (b'related_links', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))]))])), (b'half_width_link_blob_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, icon=b'title')), (b'link_blobs', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))])))])), (b'well', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Well'))])), (b'table', wagtail.wagtailcore.blocks.StructBlock([(b'headers', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(max_length=20))), (b'rows', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StreamBlock([(b'hyperlink', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'text', wagtail.wagtailcore.blocks.CharBlock(max_length=20)), (b'text_blob', wagtail.wagtailcore.blocks.TextBlock()), (b'rich_text_blob', wagtail.wagtailcore.blocks.RichTextBlock())])))])), (b'contact', wagtail.wagtailcore.blocks.StructBlock([(b'header', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'contact', wagtail.wagtailsnippets.blocks.SnippetChooserBlock(v1.models.snippets.Contact))])), (b'formfield_with_button', wagtail.wagtailcore.blocks.StructBlock([(b'btn_text', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'required', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'id', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Type of form i.e emailForm, submission-form. Should be unique if multiple forms are used', max_length=100, required=False)), (b'info', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Disclaimer')), (b'label', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), (b'type', wagtail.wagtailcore.blocks.ChoiceBlock(required=False, choices=[(b'text', b'Text'), (b'checkbox', b'Checkbox'), (b'email', b'Email'), (b'number', b'Number'), (b'url', b'URL'), (b'radio', b'Radio')])), (b'placeholder', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False))]))], blank=True),
        ),
    ]
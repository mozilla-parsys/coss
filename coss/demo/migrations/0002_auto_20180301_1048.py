# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 10:48
from __future__ import unicode_literals

import coss.global_components.blocks
import coss.global_components.models
from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demopage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('footer', coss.global_components.blocks.FooterChooserBlock(coss.global_components.models.Footer)), ('full_width_feature', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(help_text='Add a headline for the feature.', max_length=255, required=False)), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(help_text='Add a paragraph with the feature content.', required=False)), ('cta', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(help_text='Add the text for "call to action".', max_length=255, required=False)), ('url', wagtail.wagtailcore.blocks.URLBlock(help_text='Add the URL for "call to action".', required=False))))), ('background_image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text='Add a background image for this feature.', required=False))))))),
        ),
    ]

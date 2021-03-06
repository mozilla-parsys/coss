# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-15 11:42
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('global_components', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='footer_items',
            field=wagtail.wagtailcore.fields.StreamField((('entry', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('icon', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('url_name', wagtail.wagtailcore.blocks.CharBlock(help_text='Add the name of the link.', max_length=255, required=True)), ('url', wagtail.wagtailcore.blocks.URLBlock(required=True))), label='Footer Entry'))),)),
        ),
    ]

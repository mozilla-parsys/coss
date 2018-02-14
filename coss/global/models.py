from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsnippets.models import register_snippet


class FooterItemBlock(blocks.StructBlock):
    icon = ImageChooserBlock(required=True)
    url = blocks.URLBlock(required=True)


@register_snippet
class Footer(models.Model):
    footer_title = models.CharField(max_length=255,
                                    help_text='Add a short description for this footer.')
    # A list of many sub blocks of the same type (FooterItemBlock)
    footer_items = StreamField([
        ('entry', blocks.ListBlock(FooterItemBlock(label='Footer Entry')),),
    ])

    panels = [
        FieldPanel('footer_title'),
        StreamFieldPanel('footer_items')
    ]

    def __str__(self):
        return self.footer_title

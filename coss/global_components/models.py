from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.snippets.models import register_snippet


class FooterItemBlock(blocks.StructBlock):
    icon = ImageChooserBlock(required=True)
    url_name = blocks.CharBlock(max_length=255, required=True,
                                help_text='Add the name of the link.')
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


class FooterChooserBlock(SnippetChooserBlock):

    class Meta:
        template = 'tags/footer.jinja'

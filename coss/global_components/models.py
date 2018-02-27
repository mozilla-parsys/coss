from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailsnippets.blocks import SnippetChooserBlock


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


class CTABlock(blocks.StructBlock):
    text = blocks.CharBlock(
        max_length=255, required=False,
        help_text='Add the text for "call to action".')
    url = blocks.URLBlock(
        required=False,
        help_text='Add the URL for "call to action".')


class FullWidthFeatureBlock(blocks.StructBlock):
    headline = blocks.CharBlock(
        max_length=255, required=False,
        help_text='Add a headline for the feature.')
    paragraph = blocks.TextBlock(
        required=False,
        help_text='Add a paragraph with the feature content.')
    cta = CTABlock()
    background_image = ImageChooserBlock(
        required=False,
        help_text='Add a background image for this feature.')

    class Meta:
        template = 'blocks/full_width_feature.jinja'

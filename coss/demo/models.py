from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel

from coss.global_components.models import HeaderNav, Footer
from coss.global_components.blocks import FullWidthFeatureBlock


class DemoPage(Page):
    body = StreamField([
        ('full_width_feature', FullWidthFeatureBlock())
    ])
    footer = models.ForeignKey(Footer,
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL,
                               related_name='+')
    header = models.ForeignKey(HeaderNav,
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL,
                               related_name='+')

    content_panels = Page.content_panels + [
        FieldPanel('title'),
        SnippetChooserPanel('header'),
        StreamFieldPanel('body'),
        SnippetChooserPanel('footer'),
    ]
    template = 'demo/demo_page.jinja'

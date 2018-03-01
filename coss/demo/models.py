from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField

from coss.global_components.models import Footer, FooterChooserBlock


class DemoPage(Page):
    body = StreamField([
        ('footer', FooterChooserBlock(Footer)),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
    template = 'demo/demo_page.jinja'

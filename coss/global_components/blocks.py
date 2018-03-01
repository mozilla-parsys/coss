from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsnippets.blocks import SnippetChooserBlock


class FooterItemBlock(blocks.StructBlock):
    icon = ImageChooserBlock(required=True)
    url_name = blocks.CharBlock(max_length=255, required=True,
                                help_text='Add the name of the link.')
    url = blocks.URLBlock(required=True)

    class Meta:
        template = 'tags/footer.jinja'


class FooterChooserBlock(SnippetChooserBlock):

    class Meta:
        template = 'tags/footer.jinja'


class BaseLineTextBlock(blocks.StructBlock):
    """Base Structblock class to keep things DRY."""
    display_text = blocks.CharBlock(default='',
                                    label='Please input the display text here.')


class ExternalLinkBlock(BaseLineTextBlock):
    """Block that holds a link to any URL."""
    url = blocks.URLBlock()

    class Meta:
        template = 'blocks/external_link_block.jinja'


class PageLinkBlock(BaseLineTextBlock):
    """Block that holds a Wagtail Page."""
    page = blocks.PageChooserBlock()

    class Meta:
        template = 'blocks/page_link_block.jinja'


class LinkChildrenBlock(blocks.StructBlock):
    """Base class block to add second level menus (children)."""
    submenus = blocks.StreamBlock(
        [
            ('external_link', ExternalLinkBlock(),),
            ('page_link', PageLinkBlock(),),
        ]
    )


class ExternalLinkWithChildrenBlock(LinkChildrenBlock, ExternalLinkBlock):
    """Uses LinkChildrenBlock as a mixin to create an ExternalLinkBlock that supports Children."""
    pass


class PageLinkWithChildrenBlock(LinkChildrenBlock, PageLinkBlock):
    """
    Uses LinkChildrenBlock as a mixin to create a PageLinkBlock that supports Children.
    """
    pass


class FullWidthFeatureBlock(blocks.StructBlock):
    headline = blocks.CharBlock(
        max_length=255, required=False,
        help_text='Add a headline for the feature.')
    paragraph = blocks.TextBlock(
        required=False,
        help_text='Add a paragraph with the feature content.')
    cta = ExternalLinkBlock()
    background_image = ImageChooserBlock(
        required=False,
        help_text='Add a background image for this feature.')

    class Meta:
        template = 'blocks/full_width_feature.jinja'

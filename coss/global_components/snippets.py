from wagtail.wagtailsnippets.blocks import SnippetChooserBlock


class FooterChooserBlock(SnippetChooserBlock):

    class Meta:
        template = 'tags/footer.jinja'

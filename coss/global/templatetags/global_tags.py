from django_jinja import library
from jinja2 import contextfunction

from ..models import Footer


@library.global_function
@library.render_with('tags/footer.jinja')
@contextfunction
def footer_tag(context):
    return {
        'footers': Footer.objects.all(),
        'request': context['request']
    }

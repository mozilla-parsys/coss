from django_jinja import library
from jinja2 import contextfunction

from ..models import Footer


@library.global_function
@contextfunction
def footer_tag(context):
    return {
        'footers': Footer.objects.all(),
        'request': context['request']
    }

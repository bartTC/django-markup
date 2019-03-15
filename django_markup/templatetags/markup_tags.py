from django.template import Library
from django.utils.safestring import mark_safe

from django_markup.markup import formatter

register = Library()


@register.filter
def apply_markup(text, filter_name):
    return mark_safe(formatter(text, filter_name))

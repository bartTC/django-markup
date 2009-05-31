from django.template import Library
from django_markup.markup import formatter

register = Library()

@register.filter
def apply_markup(text, filter_name):
    return formatter(text, filter_name)
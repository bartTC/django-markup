.. usage-models:

Usage in models
===============

django-markup provides a ``MarkupField``, a CharField that displays a list
of :ref:`filter`::

    from django_markup.fields import MarkupField

    class Entry(models.Model):
        content = models.TextField()
        markup = MarkupField(default='restructuredtext')

Usage in a template::

    {% load markup_tags %}
    
    {% for entry in entry_list %}
        {{ entry.content|apply_markup:entry.markup }}
    {% endfor %}

The list of :ref:Filter can been overridden in your settings.py with a tuple
called ``MARKUP_CHOICES`` which holds a list of filters. A default value would
be::

    MARKUP_CHOICES = (
        'none',
        'linebreaks',
        'markdown',
        'restructuredtext',
    )
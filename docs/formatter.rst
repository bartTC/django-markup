.. _formatter:

MarkupFormatter
===============

A ``MarkupFormatter`` instance is the central point that holds :ref:`filter`
and handles the text transformation. A generic instance of ``MarkupFormatter``
is already provided with django-markup and located in::

    django_markup.markup.formatter

This instance takes 2 arguments, first the ``text`` to transform and a ``filter_name``
of the filter which should been used to convert the text. Example::

    from django_markup.markup import formatter
    print formatter('This is *markdown* text', filter_name='markdown')

You can pass any other keyword arguments which gets passed through the
filter's render function. See this example::

    from django_markup.markup import formatter
    print formatter('This is *markdown* text', filter_name='markdown', safe_mode=True)

The ``safe_mode=True`` argument gets passed to the ``render``
method of the :ref:`filter-markdown` filter and at the end passed through the
``markdown`` function itself.

For a more generic use, see :ref:`filter-settings`.


Automatically loaded filter:
============================

A bunch of :ref:`filter` are loaded loaded automatically in the
``django_markup.markup.formatter`` class. Within your settings.py you can
define which :ref:`filter` are loaded from start. A default value would be::

    from django_markup.filter.creole_filter import CreoleMarkupFilter
    # other filter...
    
    MARKUP_FILTER = {
        'creole': CreoleMarkupFilter,
        'linebreaks': LinebreaksMarkupFilter,
        'markdown': MarkdownMarkupFilter,
        'none': NoneMarkupFilter,
        'restructuredtext': RstMarkupFilter,
        'smartypants': SmartyPantsMarkupFilter,
        'textile': TextileMarkupFilter,
    }

Add a filter to a formatter instance:
=====================================

To add a :ref:`filter` to a ``MarkupFormatter`` instance, simply register it. 
Provide a filter name -- the key that is used in the templatetag to define the
filter -- and the filter class to the HtmlFormatter ``register`` method::

    from django_markup.markup import formatter
    formatter.register('uppercase', UppercaseMarkupFilter)

Update a filter
---------------

If you want to update/replace a Filter class, use the ``update`` method of the
``HtmlFormatter`` instance. Similar to registering::

    from django_markup.markup import formatter
    formatter.update('uppercase', UppercaseMarkupFilter)
    
Remove a filter
---------------

To remove a filter from the ``HtmlFormatter`` instance, simply unregister it
using the ``unregister`` method with it's filter name::

    from django_markup.markup import formatter
    formatter.unregister('uppercase')


.. _filter-settings:

Overriding filter settings
==========================

Fallback filter
---------------

It's possible to set a *fallback* filter name. This filter is taken, if you
provide no ``filter_name`` to the formatter-instance::

    print formatter('This is *markdown* text', filter_name=None)

    {{ entry.content|apply_markup:"" }}

In this case, add a variable in your ``settings.py`` called
``MARKUP_FILTER_FALLBACK``::

    MARKUP_FILTER_FALLBACK = 'linebreaks'

With this, the above examples would converted using the ``linebreaks`` filter.

Arguments to the markup filter
------------------------------

You can pass arguments to the markup-filter itself. Here is a real world
example::

    MARKUP_SETTINGS = {
        'restructuredtext': {
            'settings_overrides': {
                'initial_header_level': 2,
                'doctitle_xform': False,
                'footnote_references': 'superscript',
                'trim_footnote_reference_space': True,
                'default_reference_context': 'view',
                'link_base': ''
            }
        }

        'markdown': {
            'safe_mode': True,
            'extensions': ('tables', )
        }
    }

With the above setting, the call of the markdown function would like::

    markdown.markdown(text, safe_mode=True, extensions=('tables',))

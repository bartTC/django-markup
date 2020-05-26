.. _filter-markdown:

Markdown
========

- Filter name: ``markdown``
- Pypi package: ``Markdown``, ``bleach``, ``bleach-whitelist``

This filter comes with default settings::

    {
        'safe_mode': True
    }

You can override them by either subclassing the related ``MarkupFilter``
class or using the global settings::

    MARKUP_SETTINGS = {
        'markdown': {
            'safe_mode': True
        }
    }

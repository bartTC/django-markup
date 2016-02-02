================
reStructuredText
================

- Filter name: ``restructuredtext``
- Pypi package: ``Docutils``

This filter converts a reStructuredText_ string to HTML. See a
`quick reference`_ about reStructuredText.

This filter comes with default settings::

    {
        'settings_overrides': {
            'raw_enabled': False,
            'file_insertion_enabled': False,
        }
    }

You can override them by either subclassing the related ``MarkupFilter``
class or using the global settings::

   MARKUP_SETTINGS = {
      'restructuredtext': {
         'settings_overrides': {
            'raw_enabled': True,
            'file_insertion_enabled': True,
         }
      }
   }


.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _quick reference: http://docutils.sourceforge.net/docs/user/rst/quickref.html

.. _filter-settings:

Overriding filter settings
==========================

This section is not yet documented. Please see the sourcecode for details.
Here is a real world example::

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
        }
    }
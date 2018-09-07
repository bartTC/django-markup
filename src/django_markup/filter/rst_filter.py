from __future__ import unicode_literals

from django_markup.filter import MarkupFilter

class RstMarkupFilter(MarkupFilter):
    """
    Converts a reStructuredText string to HTML. If the pygments library is
    installed you can use a special `sourcecode` directive to highlight
    portions of your text. Example:

    .. sourcecode: python

        def foo():
            return 'foo'
    """
    title = 'reStructuredText'
    rst_part_name = 'html_body'
    kwargs = {
        'settings_overrides': {
            'raw_enabled': False,
            'file_insertion_enabled': False,
        }
    }

    def render(self, text, **kwargs):
        if kwargs:
            self.kwargs = self.kwargs.copy()
            kwargs = kwargs.copy()
            if 'settings_overrides' in kwargs:
                settings_overrides = self.kwargs['settings_overrides'].copy()
                settings_overrides.update(kwargs['settings_overrides'])
                kwargs['settings_overrides'] = settings_overrides
            self.kwargs.update(kwargs)
        from docutils import core
        publish_args = {'source': text, 'writer_name': 'html4css1'}
        publish_args.update(**self.kwargs)
        parts = core.publish_parts(**publish_args)
        return parts[self.rst_part_name]

from django_markup.filter import MarkupFilter

class MarkdownMarkupFilter(MarkupFilter):
    """
    Applies Markdown conversion to a string, and returns the HTML.
    """
    title = 'Markdown'
    kwargs = {
        'safe_mode': True,
    }

    def render(self, text, **kwargs):
        if kwargs:
            self.kwargs.update(kwargs)
        from markdown import markdown
        return markdown(text, **self.kwargs)

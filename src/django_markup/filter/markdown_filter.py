from django_markup.filter import MarkupFilter

class MarkdownMarkupFilter(MarkupFilter):
    """
    Applies Markdown conversion to a string, and returns the HTML.
    """
    title = 'Markdown'

    def render(self, text, **kwargs):
        from markdown import markdown
        return markdown(text, **kwargs)

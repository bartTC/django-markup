from django_markup.filter import MarkupFilter


class MarkdownMarkupFilter(MarkupFilter):
    """
    Applies Markdown conversion to a string, and returns the HTML.
    """

    title = 'Markdown'
    kwargs = {'safe_mode': True}

    def render(self, text, **kwargs):
        if kwargs:
            self.kwargs.update(kwargs)

        from markdown import markdown

        text = markdown(text, **self.kwargs)

        # Markdowns safe_mode is deprecated. We replace it with  Bleach
        # to keep it backwards compatible.
        # https://python-markdown.github.io/change_log/release-2.6/#safe_mode-deprecated
        if self.kwargs.get('safe_mode') is True:
            from bleach_whitelist import markdown_tags, markdown_attrs
            from bleach import clean

            text = clean(text, markdown_tags, markdown_attrs)

        return text

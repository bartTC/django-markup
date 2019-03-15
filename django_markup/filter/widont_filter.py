from django_markup.filter import MarkupFilter

class WidontMarkupFilter(MarkupFilter):
    title = 'Widont'

    def render(self, text, **kwargs):
        return '&nbsp;'.join(text.strip().rsplit(' ', 1))
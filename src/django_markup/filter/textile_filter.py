from django_markup.filter import MarkupFilter

class TextileMarkupFilter(MarkupFilter):
    title = 'Textile'

    def render(self, text, **kwargs):
        from textile import textile
        return textile(text, **kwargs)
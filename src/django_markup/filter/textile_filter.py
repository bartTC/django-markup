from django_markup.filter import MarkupFilter

class TextileMarkupFilter(MarkupFilter):
    title = 'Textile'
    is_choice = True

    def render(self, **kwargs):
        from textile import textile
        return textile(self.text, **kwargs)
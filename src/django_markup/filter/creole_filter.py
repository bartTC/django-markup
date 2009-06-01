from django_markup.filter import MarkupFilter

class CreoleMarkupFilter(MarkupFilter):
    title = 'Creole (Wiki Syntax)'

    def render(self, text, **kwargs):
        from creoleparser import creole2html
        return creole2html(text)
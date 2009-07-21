from django_markup.filter import MarkupFilter

class CreoleMarkupFilter(MarkupFilter):
    title = 'Creole (Wiki Syntax)'

    def render(self, text, **kwargs):
        from django_markup.bundles.WikiCreole.creole import Parser
        from django_markup.bundles.WikiCreole.creole2html import HtmlEmitter
        return HtmlEmitter(Parser(text).parse()).emit()
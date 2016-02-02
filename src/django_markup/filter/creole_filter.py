from django_markup.filter import MarkupFilter



class CreoleMarkupFilter(MarkupFilter):
    title = 'Creole (Wiki Syntax)'

    def render(self, text, **kwargs):
        from creole.parser import Parser
        from creole.html_emitter import HtmlEmitter
        return HtmlEmitter(Parser(text).parse()).emit()

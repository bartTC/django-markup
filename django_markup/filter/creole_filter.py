from django_markup.filter import MarkupFilter


class CreoleMarkupFilter(MarkupFilter):
    title = "Creole (Wiki Syntax)"

    def render(self, text, **kwargs):  # noqa: ARG002 Unused argument
        from creole import creole2html

        return creole2html(text)

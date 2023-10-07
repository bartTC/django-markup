from django_markup.filter import MarkupFilter


class WidontMarkupFilter(MarkupFilter):
    title = "Widont"

    def render(self, text, **kwargs):  # noqa: ARG002 Unused argument
        return "&nbsp;".join(text.strip().rsplit(" ", 1))

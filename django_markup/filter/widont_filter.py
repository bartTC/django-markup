from typing import Any, Self

from django_markup.filter import MarkupFilter


class WidontMarkupFilter(MarkupFilter):
    title = "Widont"

    def render(
        self: Self,
        text: str,
        **kwargs: Any,  # noqa: ARG002 Unused argument
    ) -> str:
        return "&nbsp;".join(text.strip().rsplit(" ", 1))

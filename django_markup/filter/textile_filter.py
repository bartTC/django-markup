from typing import Any, Self

from django_markup.filter import MarkupFilter


class TextileMarkupFilter(MarkupFilter):
    title = "Textile"

    def render(
        self: Self,
        text: str,
        **kwargs: Any,  # Unused argument
    ) -> str:
        from textile import textile

        return textile(text, **kwargs)

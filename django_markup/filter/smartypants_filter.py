from typing import Any, Self

from django_markup.filter import MarkupFilter


class SmartyPantsMarkupFilter(MarkupFilter):
    title = "SmartyPants"

    def render(
        self: Self,
        text: str,
        **kwargs: Any,  # Unused argument
    ) -> str:
        from smartypants import smartypants

        return smartypants(text, **kwargs)

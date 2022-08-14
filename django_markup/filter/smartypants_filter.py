from django_markup.filter import MarkupFilter


class SmartyPantsMarkupFilter(MarkupFilter):
    title = "SmartyPants"

    def render(self, text, **kwargs):
        from smartypants import smartypants

        return smartypants(text, **kwargs)

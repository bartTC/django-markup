from django_markup.filter import MarkupFilter

class SmartyPantsMarkupFilter(MarkupFilter):
    title = 'SmartyPants'

    def render(self, **kwargs):
        from smartypants import SmartyPants
        return SmartyPants(self.text, **kwargs)
from django_markup.filter import MarkupFilter

class LightboxMarkupFilter(MarkupFilter):
    '''Add's a lightbox attributes to links that have images in it's target'''
    title = 'Lightbox Attribute'

    def __init__(self):
        import re
        self.r_lightbox = re.compile('<a (?=[^>]*\.(jpg|gif|png))(?![^>]*lightbox)')
        self.s_lightbox = '<a rel="lightbox" '

    def render(self, text, attribute='rel="lightbox"', **kwargs):
        return self.r_lightbox.sub(self.s_lightbox, text)
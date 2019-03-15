class MarkupFilter(object):
    """
    Abstract your new filters from this class. This is the most simplest way of
    a filter, it accepts the text in it's render method and returns it, as is.
    """
    title = 'BaseFilter'

    def render(self, text, **kwargs):
        return text
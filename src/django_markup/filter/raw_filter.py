from django_markup.filter import MarkupFilter

class RawMarkupFilter(MarkupFilter):
    """
    Simply returns the text without any modification. This is the same as the
    base class does.
    """
    title = 'Raw (no processing)'
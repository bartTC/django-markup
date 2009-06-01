
class MarkupFilter(object):
    """
    Abstract your new filters from this class. This is the most simplest way of
    a filter, it accepts the text in it's __init__ method and the render method
    returns it, as is.
    """
    title = 'BaseFilter'

    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text

# The list of automatically loaded MarkupFilters
from django_markup.filter.linebreaks_filter import LinebreaksMarkupFilter
from django_markup.filter.markdown_filter import MarkdownMarkupFilter
from django_markup.filter.textile_filter import TextileMarkupFilter
from django_markup.filter.rst_filter import RstMarkupFilter
from django_markup.filter.smartypants_filter import SmartyPantsMarkupFilter
from django_markup.filter.raw_filter import RawMarkupFilter
from django_markup.filter.creole_filter import CreoleMarkupFilter

# MarkupFilter that get's loaded automatically
# You can override this list within your settings.

DEFAULT_MARKUP_FILTER = {
    'creole': CreoleMarkupFilter,
    'linebreaks': LinebreaksMarkupFilter,
    'markdown': MarkdownMarkupFilter,
    'raw': RawMarkupFilter,
    'restructuredtext': RstMarkupFilter,
    'smartypants': SmartyPantsMarkupFilter,
    'textile': TextileMarkupFilter,
}

# MarkupFilter that are the default value for choices, used in the MarkupField
# You can override this list within your settings.

DEFAULT_MARKUP_CHOICES = (
    'linebreaks',
    'markdown',
    'restructuredtext',
)
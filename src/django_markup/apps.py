from django.apps.config import AppConfig

# The list of automatically loaded MarkupFilters
from .filter.linebreaks_filter import LinebreaksMarkupFilter
from .filter.markdown_filter import MarkdownMarkupFilter
from .filter.textile_filter import TextileMarkupFilter
from .filter.rst_filter import RstMarkupFilter
from .filter.smartypants_filter import SmartyPantsMarkupFilter
from .filter.none_filter import NoneMarkupFilter
from .filter.creole_filter import CreoleMarkupFilter
from .filter.widont_filter import WidontMarkupFilter


class DjangoMarkupConfig(AppConfig):
    name = 'django_markup'
    verbose_name = "django-markup"

    # MarkupFilter that get's loaded automatically
    # You can override this list within your settings: MARKUP_FILTER
    markup_filter = {
        'creole': CreoleMarkupFilter,
        'linebreaks': LinebreaksMarkupFilter,
        'markdown': MarkdownMarkupFilter,
        'none': NoneMarkupFilter,
        'restructuredtext': RstMarkupFilter,
        'smartypants': SmartyPantsMarkupFilter,
        'textile': TextileMarkupFilter,
        'widont': WidontMarkupFilter,
    }

    # If the formatter instance is invoked without a filter_name, this is the
    # one we fallback to. E.g. `linebreaks`.
    markup_filter_fallback = None

    # MarkupFilter that are the default value for choices, used in the MarkupField
    # You can override this list within your settings: MARKUP_CHOICES
    markup_choices = (
        'none',
        'linebreaks',
        'markdown',
        'restructuredtext',
    )

    markup_settings = None

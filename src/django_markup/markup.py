from django.conf import settings
from django.utils.safestring import mark_safe

class MarkupFormatter(object):

    def __init__(self):
        self.filter_list = {}

    def _get_filter_title(self, filter_name):
        '''
        Returns the human readable title of a given filter_name. If no title
        attribute is set, the filter_name is used, where underscores are
        replaced with whitespaces and the first character of each word is
        uppercased. Example:

        >>> MarkupFormatter._get_title('markdown')
        'Markdown'

        >>> MarkupFormatter._get_title('a_cool_filter_name')
        'A Cool Filter Name'
        '''
        title = getattr(self.filter_list[filter_name], 'title', None)
        if not title:
            title = ' '.join([w.title() for w in filter_name.split('_')])
        return title

    def choices(self):
        '''
        Returns the filter list as a tuple. Useful for model choices.

        To quickly remove a filter from the choice list, set it's is_choice
        attribute to false:

            formatter.filter_list['markdown'].is_choice = False
        '''
        choices = []
        for f in self.filter_list.iterkeys():
            if getattr(self.filter_list[f], 'is_choice', False):
                choices.append((f, self._get_filter_title(f)))
        return choices

    def register(self, filter_name, filter_func):
        '''
        Register a new filter for use
        '''
        self.filter_list[filter_name] = filter_func

    def unregister(self, filter_name):
        '''
        Unregister a filter from the filter list
        '''
        if filter_name in self.filter_list:
            self.filter_list.pop(filter_name)

    def __call__(self, text, filter_name, **kwargs):
        '''
        Applies text-to-HTML conversion to a string, and returns the
        HTML.
        '''
        # Check that the filter_name is a registered markup filter
        if filter_name not in self.filter_list:
            raise ValueError("'%s' is not a registered markup filter. Registered filters are: %s." %
                             (filter_name, ', '.join(self.filter_list.iterkeys())))

        filter_func = self.filter_list[filter_name]

        # Get additional settings for the filter_func and apply **kwargs on it
        filter_kwargs = {}
        filter_settings = getattr(settings, 'MARKUP_SETTINGS', None)
        if filter_settings and filter_name in filter_settings:
            filter_kwargs = filter_settings[filter_name]
        filter_kwargs.update(**kwargs)

        # Apply the filter on text
        text = filter_func(text, **filter_kwargs)

        # Return a safe string unless filter_func.mark_safe is explicitly False
        if getattr(filter_func, 'mark_safe', True):
            return mark_safe(text)

        # Otherwise return the text as is
        return text

# Unless you need to have multiple instances of MarkupFormatter lying
# around, or want to subclass it, the easiest way to use it is to
# import this instance.
#
# Note if you create a new instance of MarkupFormatter(), the built
# in filters are not assigned.

formatter = MarkupFormatter()

# Assign the built in filters to the default formatter
from django_markup.defaults import DEFAULT_MARKUP_FILTERS
for filter_name, filter_func in DEFAULT_MARKUP_FILTERS.items():
    formatter.register(filter_name, filter_func)
from django.conf import settings
from django_markup.defaults import DEFAULT_MARKUP_FILTER, DEFAULT_MARKUP_CHOICES

class MarkupFormatter(object):

    def __init__(self, load_defaults=True):
        self.filter_list = {}

        if load_defaults:
            filter_list = getattr(settings, 'MARKUP_FILTER', DEFAULT_MARKUP_FILTER)
            for filter_name, filter_class in filter_list.iteritems():
                self.register(filter_name, filter_class)

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
        '''
        choice_list = getattr(settings, 'MARKUP_CHOICES', DEFAULT_MARKUP_CHOICES)
        return [(f, self._get_filter_title(f)) for f in choice_list]

    def register(self, filter_name, filter_class):
        '''
        Register a new filter for use
        '''
        self.filter_list[filter_name] = filter_class

    def update(self, filter_name, filter_class):
        '''
        Yep, this is the same as register, it just sounds better.
        '''
        self.filter_list[filter_name] = filter_class

    def unregister(self, filter_name):
        '''
        Unregister a filter from the filter list
        '''
        if filter_name in self.filter_list:
            self.filter_list.pop(filter_name)

    def flush(self):
        '''
        Flushes the filter list.
        '''
        self.filter_list = {}

    def __call__(self, text, filter_name=None, **kwargs):
        '''
        Applies text-to-HTML conversion to a string, and returns the
        HTML.

        TODO: `filter` should either be a filter_name or a filter class.
        '''

        filter_fallback = getattr(settings, 'MARKUP_FILTER_FALLBACK', False)
        if not filter_name and filter_fallback:
            filter_name = filter_fallback

        # Check that the filter_name is a registered markup filter
        if filter_name not in self.filter_list:
            raise ValueError("'%s' is not a registered markup filter. Registered filters are: %s." %
                             (filter_name, ', '.join(self.filter_list.iterkeys())))
        filter_class = self.filter_list[filter_name]

        # Read global filter settings and apply it
        filter_kwargs = {}
        filter_settings = getattr(settings, 'MARKUP_SETTINGS', {})
        if filter_name in filter_settings:
            filter_kwargs.update(filter_settings[filter_name])
        filter_kwargs.update(**kwargs)

        # Apply the filter on text
        return filter_class().render(text, **filter_kwargs)


# Unless you need to have multiple instances of MarkupFormatter lying
# around, or want to subclass it, the easiest way to use it is to
# import this instance.
#
# Note if you create a new instance of MarkupFormatter(), the built
# in filters are not assigned.

formatter = MarkupFormatter()
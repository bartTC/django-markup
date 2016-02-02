from __future__ import unicode_literals

from django.test import TestCase

from ..markup import formatter
from ..templatetags.markup_tags import apply_markup
from .markup_strings import S

class MarkupTestCase(TestCase):
    longMessage = True
    filterList = (
        'none',
        'linebreaks',
        'markdown',
        'textile',
    )

    def test_templatetag_in_python(self):
        """
        Markup formatting from the Python side using the templatetag directly.
        """
        for filter_name in self.filterList:
            text, expected = S[filter_name]
            msg = 'Failed test for filter "{}"'.format(filter_name)
            result = apply_markup(text, filter_name)
            self.assertEqual(result, expected, msg)

    def test_formatter_method(self):
        """
        The generic MarkupFormatter instance.
        """
        for filter_name in self.filterList:
            text, expected = S[filter_name]
            msg = 'Failed test for filter "{}"'.format(filter_name)
            result = formatter(text, filter_name=filter_name)
            self.assertEqual(result, expected, msg)

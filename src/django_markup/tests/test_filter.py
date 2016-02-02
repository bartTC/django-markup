from __future__ import unicode_literals

from django.test import TestCase

from ..markup import formatter
from ..templatetags.markup_tags import apply_markup
from .markup_strings import MARKUP_TESTS

class MarkupTestCase(TestCase):
    longMessage = True


    def test_templatetag_in_python(self):
        """
        Markup formatting from the Python side using the templatetag directly.
        """
        for T in MARKUP_TESTS:
            filter, text, expected = T.values()
            msg = 'Failed test for filter "{}"'.format(filter)
            result = apply_markup(text, filter)
            self.assertEqual(result, expected, msg)

    def test_formatter_method(self):
        """
        The generic MarkupFormatter instance.
        """
        for T in MARKUP_TESTS:
            filter, text, expected = T.values()
            msg = 'Failed test for filter "{}"'.format(filter)
            result = formatter(text, filter_name=filter)
            self.assertEqual(result, expected, msg)

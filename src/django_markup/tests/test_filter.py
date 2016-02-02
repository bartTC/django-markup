from __future__ import unicode_literals

import six
import os
from django.test import TestCase

from ..markup import formatter
from . import markup_strings as s

FILES_DIR = os.path.join(os.path.dirname(__file__), 'files')


class FormatterTestCase(TestCase):
    """
    Test the Formatter conversion done in Python of all shipped filters.
    """
    def test_none_filter(self):
        text, expected = s.NONE
        result = formatter(text, filter_name='none')
        self.assertEqual(result, expected)

    def test_linebreaks_filter(self):
        text, expected = s.LINEBREAKS
        result = formatter(text, filter_name='linebreaks')
        self.assertEqual(result, expected)

    def test_markdown_filter(self):
        text, expected = s.MARKDOWN
        result = formatter(text, filter_name='markdown')
        self.assertEqual(result, expected)

    def test_textile_filter(self):
        text, expected = s.TEXTILE
        result = formatter(text, filter_name='textile')
        self.assertEqual(result, expected)

    def test_rst_filter(self):
        text, expected = s.RST
        result = formatter(text, filter_name='restructuredtext')
        self.assertEqual(result, expected)

    def test_rst_header_levels(self):
        """
        Make sure the rST filter fetches the entire document rather just the
        document fragment.

        :see: https://github.com/bartTC/django-markup/issues/14
        """
        text = open(os.path.join(FILES_DIR, 'rst_header.txt')).read()
        expected = open(os.path.join(FILES_DIR, 'rst_header_expected.txt')).read()
        result = formatter(text, filter_name='restructuredtext')
        self.assertEqual(result, expected)

    def test_creole_filter(self):
        text, expected = s.CREOLE
        result = formatter(text, filter_name='creole')
        self.assertEqual(result, expected)

    def test_smartypants_filter(self):
        text, expected = s.SMARTYPANTS
        result = formatter(text, filter_name='smartypants')
        self.assertEqual(result, expected)

    def test_widont_filter(self):
        text, expected = s.WIDONT
        result = formatter(text, filter_name='widont')
        self.assertEqual(result, expected)


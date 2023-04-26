import os

from django.test import TestCase

from ..markup import formatter
from . import markup_strings as s

FILES_DIR = os.path.join(os.path.dirname(__file__), "files")


class FormatterTestCase(TestCase):
    """
    Test the Formatter conversion done in Python of all shipped filters.
    """

    def test_unregistered_filter_fails_loud(self):
        """
        Trying to call a unregistered filter will raise a ValueError.
        """
        self.assertRaises(
            ValueError,
            formatter,
            "some text",
            filter_name="does-not-exist",
        )

    def test_none_filter(self):
        text, expected = s.NONE
        result = formatter(text, filter_name="none")
        self.assertEqual(result, expected)

    def test_linebreaks_filter(self):
        text, expected = s.LINEBREAKS
        result = formatter(text, filter_name="linebreaks")
        self.assertEqual(result, expected)

    def test_markdown_filter(self):
        text, expected = s.MARKDOWN
        result = formatter(text, filter_name="markdown")
        self.assertEqual(result, expected)

    def test_markdown_filter_pre(self):
        text, expected = s.MARKDOWN_PRE
        result = formatter(text, filter_name="markdown")
        self.assertEqual(result, expected)

    def test_markdown_safemode_enabled_by_default(self):
        """Safe mode is enabled by default."""
        text, expected = s.MARKDOWN_JS_LINK
        result = formatter(text, filter_name="markdown")
        self.assertEqual(result, expected)

    def test_textile_filter(self):
        text, expected = s.TEXTILE
        result = formatter(text, filter_name="textile")
        self.assertEqual(result, expected)

    def test_rst_filter(self):
        text, expected = s.RST
        result = formatter(text, filter_name="restructuredtext")
        self.assertEqual(result, expected)

    def test_rst_header_levels(self):
        """
        Make sure the rST filter fetches the entire document rather just the
        document fragment.

        :see: https://github.com/bartTC/django-markup/issues/14
        """
        text = open(os.path.join(FILES_DIR, "rst_header.txt")).read()
        expected = open(os.path.join(FILES_DIR, "rst_header_expected.txt")).read()
        result = formatter(text, filter_name="restructuredtext")
        self.assertEqual(result, expected)

    def test_rst_with_pygments(self):
        """
        Having Pygments installed will automatically provide a ``.. code-block``
        directive in reStructredText to highlight code snippets.
        """
        text = open(os.path.join(FILES_DIR, "rst_with_pygments.txt")).read()
        expected = open(
            os.path.join(FILES_DIR, "rst_with_pygments_expected.txt"),
        ).read()
        result = formatter(text, filter_name="restructuredtext")

        self.assertEqual(result, expected)

    def test_rst_raw_default(self):
        """Raw file inclusion is disabled by default."""
        text = open(os.path.join(FILES_DIR, "rst_raw.txt")).read()
        result = formatter(text, filter_name="restructuredtext")
        self.assertIn("Other text", result)
        self.assertNotIn("<script>", result)

    def test_rst_include_default(self):
        """File inclusion is disabled by default."""
        # Build up dynamically in order to build absolute path
        text = (
            ".. include:: "
            + os.path.join(FILES_DIR, "rst_header.txt")
            + "\n\nOther text\n"
        )
        result = formatter(text, filter_name="restructuredtext")
        self.assertIn("Other text", result)
        self.assertNotIn("Header 1", result)

    def test_creole_filter(self):
        text, expected = s.CREOLE
        result = formatter(text, filter_name="creole")
        self.assertEqual(result, expected)

    def test_smartypants_filter(self):
        text, expected = s.SMARTYPANTS
        result = formatter(text, filter_name="smartypants")
        self.assertEqual(result, expected)

    def test_widont_filter(self):
        text, expected = s.WIDONT
        result = formatter(text, filter_name="widont")
        self.assertEqual(result, expected)

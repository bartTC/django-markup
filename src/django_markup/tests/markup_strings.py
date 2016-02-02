from __future__ import unicode_literals

import os

FILES_DIR = os.path.join(os.path.dirname(__file__), 'files')

"""
Sample Markup strings and their expected pendant.
"""

MARKUP_TESTS = [
    # None filter
    {
        'filter': 'none',
        'text': '*This* is some text.',
        'expected': '*This* is some text.'
    },

    # Django's linebreaks filter
    {
        'filter': 'linebreaks',
        'text': '*This* is some text.',
        'expected': '<p>*This* is some text.</p>'
    },

    # Simple Markdown
    {
        'filter': 'markdown',
        'text': '*This* is some text.',
        'expected': '<p><em>This</em> is some text.</p>'
    },

    # Simple Textile
    {
        'filter': 'textile',
        'text': '*This* is some text.',
        'expected': '\t<p><strong>This</strong> is some text.</p>'
    },

    # Simple RestructuredText
    {
        'filter': 'restructuredtext',
        'text': '*This* is some text.',
        'expected': '<p><em>This</em> is some text.</p>\n'
    },
]

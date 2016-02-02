from __future__ import unicode_literals

"""
Sample Markup strings and their expected pendant.
"""

# Dictionary contaning the filter key
# and a tuple of (text, expected formatted text).

S = {
    'none': (
        "*This* is some text.",
        "*This* is some text."
    ),

    'linebreaks': (
        "*This* is some text.",
        "<p>*This* is some text.</p>"
    ),

    'markdown': (
        "*This* is some text.",
        "<p><em>This</em> is some text.</p>"
    ),

    'textile': (
        "*This* is some text.",
        "\t<p><strong>This</strong> is some text.</p>"
    ),

    'restructuredtext': (
        "*This* is some text.",
        "<p><strong>This</strong> is some text.</p>"
    ),
}

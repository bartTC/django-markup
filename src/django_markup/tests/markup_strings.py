from __future__ import unicode_literals

"""
Sample Markup strings and their expected pendant.
"""

NONE = (
    '*This* is some text.',
    '*This* is some text.'
)

# Django's linebreaks filter
LINEBREAKS = (
    '*This* is some text.',
    '<p>*This* is some text.</p>'

)

# Simple Markdown
MARKDOWN = (
    '*This* is some text.',
    '<p><em>This</em> is some text.</p>'
)

# Simple Textile
TEXTILE = (
    '*This* is some text.',
    '\t<p><strong>This</strong> is some text.</p>'
)

# Simple RestructuredText
RST = (
    '*This* is some text.',
    '<div class="document">\n<p><em>This</em> is some text.</p>\n</div>\n'
)

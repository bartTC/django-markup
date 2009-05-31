def linebreaks(text, **kwargs):
    """
    Replaces line breaks in plain text with appropriate HTML; a single
    newline becomes an HTML line break (``<br />``) and a new line
    followed by a blank line becomes a paragraph break (``</p>``).

    >>> linebreaks(u'Hallo Welt\nBlabla')
    u'Hallo Welt<br/>Blabla'
    """
    from django.template.defaultfilters import linebreaks
    return linebreaks(text, **kwargs)
linebreaks.title = 'Linebreaks'
linebreaks.mark_safe = True
linebreaks.is_choice = True

def textile(text, **kwargs):
    """
    Applies Textile conversion to a string, and returns the HTML.

    This is simply a pass-through to the ``textile`` template filter
    included in ``django.contrib.markup``, which works around issues
    PyTextile has with Unicode strings. If you're not using Django but
    want to use Textile with ``MarkupFormatter``, you'll need to
    supply your own Textile filter.
    """
    from django.contrib.markup.templatetags.markup import textile
    return textile(text)
textile.title = 'Textile'
textile.mark_safe = True
textile.is_choice = True

def markdown(text, **kwargs):
    """
    Applies Markdown conversion to a string, and returns the HTML.
    """
    import markdown
    return markdown.markdown(text, **kwargs)
markdown.title = 'Markdown'
markdown.mark_safe = True
markdown.is_choice = True

def restructuredtext(text, **kwargs):
    """
    Applies reStructuredText conversion to a string, and returns the
    HTML.
    """
    from docutils import core
    parts = core.publish_parts(source=text,
                               writer_name='html4css1',
                               **kwargs)
    return parts['fragment']
restructuredtext.title = 'ReStructured Text'
restructuredtext.mark_safe = True
restructuredtext.is_choice = True

def smartypants(text, **kwargs):
    """
    Applies SmartyPants to a piece of text, applying typographic
    niceties.
    """
    from smartypants import smartyPants
    return smartyPants(text, **kwargs)
smartypants.title = 'SmartyPants'
smartypants.mark_safe = True
smartypants.is_choice = False

DEFAULT_MARKUP_FILTERS = {
    'linebreaks': linebreaks,
    'textile': textile,
    'markdown': markdown,
    'restructuredtext': restructuredtext,
    'smartypants': smartypants,
}
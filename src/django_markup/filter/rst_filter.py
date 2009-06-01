from django_markup.filter import MarkupFilter

class RstMarkupFilter(MarkupFilter):
    """
    Converts a reStructuredText string to HTML. If the pygments library is
    installed you can use a special `sourcecode` directive to highlight
    portions of your text. Example:

    .. sourcecode: python

        def foo():
            return 'foo'
    """
    title = 'reStructuredText'

    def __init__(self):
        # Check if pygments is installed and load it's directive
        try:
            import pygments
            from docutils.parsers.rst import directives
            directives.register_directive('sourcecode', self.pygments_directive)
        except ImportError:
            pass

    def render(self, text, **kwargs):
        from docutils import core
        publish_args = {'source': text, 'writer_name': 'html4css1'}
        publish_args.update(**kwargs)
        parts = core.publish_parts(**publish_args)
        return parts['fragment']

    def pygments_directive(self, name, arguments, options, content, lineno,
                           content_offset, block_text, state, state_machine,
                           pygments_formatter=None):
        import pygments
        from pygments import formatters, lexers
        from docutils import nodes

        if not pygments_formatter:
            pygments_formatter = formatters.HtmlFormatter

        try:
            lexer = lexers.get_lexer_by_name(arguments[0])
        except ValueError:
            lexer = lexers.TextLexer()

        parsed = pygments.highlight(u'\n'.join(content), lexer, pygments_formatter())
        return [nodes.raw('', parsed, format='html')]
    pygments_directive.arguments = (1, 0, 1)
    pygments_directive.content = 1
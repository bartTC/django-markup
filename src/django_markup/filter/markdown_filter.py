from django_markup.filter import MarkupFilter

class MarkdownMarkupFilter(MarkupFilter):
    """
    Applies Markdown conversion to a string, and returns the HTML. If the
    pygments library is installed, it highlights code blocks with it.
    """
    title = 'Markdown'

    def render(self, **kwargs):
        from markdown import markdown
        md_text = markdown(self.text, **kwargs)

        try:
            # Check if pygments is installed and highlight code blocks.
            import pygments
            return self.pygmentize(md_text)
        except ImportError:
            # Otherwise return the unhighlighted markdown'd text
            return md_text

    def get_lexer(self, code_string, lexer_prefix='#!'):
        """
        Resolves the lexer name out of a code block.
        """
        from pygments import lexers
        from pygments.util import ClassNotFound

        lexer_line = code_string.splitlines()[0]
        if lexer_line.startswith(lexer_prefix):
            lexer_name = lexer_line[len(lexer_prefix):].strip(' ')
            code_string = '\n'.join(code_string.splitlines()[1:])
            try:
                lexer = lexers.get_lexer_by_name(lexer_name)
            except ClassNotFound:
                try:
                    lexer = lexers.guess_lexer(code_string)
                except ClassNotFound:
                    lexer = lexers.TextLexer()
        else:
            try:
                lexer = lexers.guess_lexer(code_string)
            except ClassNotFound:
                lexer = lexers.TextLexer()
        return (code_string, lexer)

    def pygmentize(self, text, pygments_formatter=None, **kwargs):
        """
        Replaces naked code blocks with highlighted.
        """
        import pygments
        import re
        regex = re.compile(r'(<pre><code>(.*?)</code></pre>)', re.DOTALL)
        last_end = 0
        to_return = ''
        found = 0
        for match_obj in regex.finditer(text):
            code_string = match_obj.group(2)
            code_string, lexer = self.get_lexer(code_string)
            pygmented_string = pygments.highlight(code_string, lexer, pygments_formatter())
            pygmented_string = pygmented_string.replace('&amp;', '&')
            to_return = to_return + text[last_end:match_obj.start(1)] + pygmented_string
            last_end = match_obj.end(1)
            found += 1
        to_return = to_return + text[last_end:]
        return to_return
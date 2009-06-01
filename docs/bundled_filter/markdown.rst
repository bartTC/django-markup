.. _filter-markdown:

Markdown
========

- Filter name: ``markdown``
- Pypi package: ``Markdown``

This filter converts a Markdown string to html. Additionally it highlights 
code blocks (in Markdown defined by an indentation of 4 spaces) if the
Pygments_ library is installed. Example::

    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut

        #!python
        def foo(bar):
            return bar
            
    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut

The code block can have a keyword (a lexer) in it's first line which defines
what language should been used to highlight the code block. Here ``python`` is
used, a lexer is prefixed with '#!'. A list of all available lexers is
available under `Pygments Lexer`_.

.. _Pygments: http://pygments.org/
.. _Pygments Lexer: http://pygments.org/docs/lexers/
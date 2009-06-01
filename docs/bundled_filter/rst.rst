================
reStructuredText
================

- Filter name: ``restructuredtext``
- Pypi package: ``Docutils``

This filter converts a reStructuredText_ string to HTML. It has a special
directive ``sourcecode`` which highlights a code-block if the Pygments_
library is installed. Example::

    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut

    .. sourcecode:: python
    
        def foo(bar):
            return bar
            
    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut

The directive ``sourcecode`` follows a keyword (a lexer) which language
should been used to highlight the code block. Here ``python`` is used. A list
of all available lexers is available under `Pygments Lexer`_.

See a `quick reference`_ about reStructuredText.

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _quick reference: http://docutils.sourceforge.net/docs/user/rst/quickref.html
.. _Pygments: http://pygments.org/
.. _Pygments Lexer: http://pygments.org/docs/lexers/

Other filters:
--------------

.. toctree::
   :maxdepth: 1
   :glob:
   
   bundled_filters/*
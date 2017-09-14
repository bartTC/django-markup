================
reStructuredText
================

- Filter name: ``restructuredtext``
- Pypi package: ``Docutils``

This filter converts a reStructuredText_ string to HTML. See a
`quick reference`_ about reStructuredText.

This filter comes with default settings::

    {
        'settings_overrides': {
            'raw_enabled': False,
            'file_insertion_enabled': False,
        }
    }

You can override them by either subclassing the related ``MarkupFilter``
class or using the global settings::

   MARKUP_SETTINGS = {
      'restructuredtext': {
         'settings_overrides': {
            'raw_enabled': True,
            'file_insertion_enabled': True,
         }
      }
   }


Syntax Highlighting:
====================

Pygments_ will automatically add a ``code-block`` directive with syntax
highlighting.

rST Input::

    Some **rST** text.
    
    .. code-block:: python
    
        def test():
          return 'Hello World'

Output::

    <div class="document">
    <p>Some <strong>rST</strong> text.</p>
    <pre class="code python literal-block">
    <span class="keyword">def</span> <span class="name function">test</span><span class="punctuation">():</span>
      <span class="keyword">return</span> <span class="literal string single">\'Hello World\'</span>
    </pre>
    </div>


By default, reStructuredText uses long class names. You can change the format
of the class names using the syntax_highlight_ option::

   MARKUP_SETTINGS = {
      'restructuredtext': {
         'settings_overrides': {
            'syntax_highlight': short,
         }
      }
   }

Above output but with `short` option::

    <div class="document">
    <p>Some <strong>rST</strong> text.</p>
    <pre class="code python literal-block">
    <span class="keyword">def</span> <span class="name function">test</span><span class="punctuation">():</span>
      <span class="keyword">return</span> <span class="literal string single">\'Hello World\'</span>
    </pre>
    </div>


.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _quick reference: http://docutils.sourceforge.net/docs/user/rst/quickref.html
.. _Pygments: http://pygments.org
.. _syntax_highlight: http://docutils.sourceforge.net/docs/user/config.html#syntax-highlight

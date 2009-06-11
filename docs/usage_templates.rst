Usage in Django templates
=========================

django-markup provides a templatetag to apply filter on variables or text.

First make sure that in every template you want to use django-markup the
template library `markup_tags` is loaded::

    {% load markup_tags %}

Then apply the ``apply_markup`` on strings or variables you want to convert.
The tag has one argument which defines the :ref:`filter` you want to apply::

    {{ entry.content|apply_markup:"markdown" }}
    {{ "One line of a *string*"|apply_markup:"markdown" }}

Of course you can apply more than one filter::

    {{ entry.content|apply_markup:"markdown"|apply_markup:"smartypants" }}

Multiline strings
-----------------

You can use this filter for multiline strings too::

    {% filter apply_markup:"markdown" %}
    # Hello World #
    
    I am a text that was converted with **markdown**!    
    {% endfilter %}

This results in::

    <h1>Hello World</h1>
    <p>I am a text that was converted with <strong>markdown</strong>!

A list of all bundled filters:
------------------------------

.. toctree::
   :maxdepth: 1
   :glob:
   
   bundled_filter/*
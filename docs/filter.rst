.. _filter:

Filter
======

A filter is a simple class that takes a text input, transforms it and
returns the transformed text. New filters must abstract a base class ``MarkupFilter``.
Let's make an example that reads a text and converts it to uppercase::


    from django_markup.filter import MarkupFilter

    class UppercaseMarkupFilter(MarkupFilter):
        title = 'Uppercase text'
        def render(self, text, **kwargs):
            return text.upper()

A filter must contain a ``render`` method that takes a variable ``text`` as it's
first argument  which holds the text to transform. Also it must accept a
``**kwargs`` argument which is used for :ref:`filter-settings`. At the end, the
``render`` method returns the modified text.

Additionally the filter class should contain an attribute ``title`` which holds a
better human readable name for this filter.

Please have a look on the sourcecode of the bundled filters for better
examples.


Adding filters to a formatter
-----------------------------

See :ref:`formatter` how to attach a filter to a formatter class.

A list of all bundled filters:
------------------------------

.. toctree::
   :maxdepth: 1
   :glob:

   bundled_filter/*
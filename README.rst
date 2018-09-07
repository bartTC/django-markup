.. image:: https://travis-ci.org/bartTC/django-markup.svg?branch=master
    :target: https://travis-ci.org/bartTC/django-markup

.. image:: https://codecov.io/github/bartTC/django-markup/coverage.svg?branch=master
    :target: https://codecov.io/github/bartTC/django-markup?branch=master

=============
django-markup
=============

This app is a generic way to provide filters that convert text into html.

The documentation is available at https://docs.elephant.house/django-markup/

Quickstart
==========

Download and install the package from the python package index (pypi)::

    pip install django-markup

Note that `django-markup` ships with some filters ready to use, but the more
complex packages such as Markdown or ReStructuredText are not part of the code.
Please refer the docs which packages are used for the built-in filter.

An alternative is to install django-markup with all filter dependencies
right away. Do so with::

    pip install django-markup[all-filter-dependencies]

Then add it to the ``INSTALLED_APPS`` list::

    INSTALLED_APPS = (
        ...
        'django_markup',
    )

Use it in the template::

    {% load markup_tags %}
    {{ the_text|apply_markup:"markdown" }}

Or in Python code::

    from django_markup.markup import formatter
    formatter('Some *Markdown* text.', filter_name='markdown')

Testsuite
=========

To run the testsuite simply run ``python setup.py test`` which will invoke a Tox
collection testing against various Python and Django versions.

For a specific local installation run ``python runtests.py``.

.. image:: https://travis-ci.org/bartTC/django-markup.svg?branch=master
    :target: https://travis-ci.org/bartTC/django-markup

.. image:: https://codecov.io/github/bartTC/django-markup/coverage.svg?branch=master
    :target: https://codecov.io/github/bartTC/django-markup?branch=master

=============
django-markup
=============

This app is a generic way to provide filters that convert text into html.

The documentation is available at http://readthedocs.org/docs/django-markup/en/latest/

Quickstart
==========

Download and install the package from the python package index (pypi)::

    pip install django-markup

Note that `django-markup` ships with some filters ready to use, but the
requirements of those filters are not installed by default! If you want to
use all of the filters right away, you can install their latest packages
with::

    pip install textile smartypants docutils markdown python-creole

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

To run the testsuite simply run `python setup.py test` which will invoke a Tox
collection testing against various Python and Django versions.

For a specific local installation run `python runtests.py`.

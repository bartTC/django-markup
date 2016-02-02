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

Changelog
=========

v1.0 (2016-01-02):
    - Removed some 5 year old dust
    - Django 1.8+ compatible
    - Tests

    Backwards incompatible changes:

    - Removed Pygments highlighting in the Markdown and RestructuredText filter.
    - Removed CreoleParser library in favor of a pypi package.
    - Removed Lightbox filter.
    - The RestructuredText filter now renders level 1 and 2 headers.
      See Github `Issue 14`_ for details and a backwards compatible workaround.

v0.4 (2011-06-1):
    - Added a widont filter
    - MarkupField is South compatible.
    - Tested with Django 1.3

v0.3 (2009-07-29):
    django-markup now ships with a builtin creole parser. Advantage is, that
    the recently used Creoleparser library needs the Genshi lib, which needs
    a c-compiler and so on. The builtin creole parser is a pure python library
    without any dependencies and follows the wikicreole.org specifications.
    django-markup uses the `WikiCreole library`_.

.. _WikiCreole library: http://devel.sheep.art.pl/creole/

.. _Issue 14: https://github.com/bartTC/django-markup/issues/14

=============
django-markup
=============

This app is a generic way to provide filters that convert text into html.

The documentation is available at http://readthedocs.org/docs/django-markup/en/latest/

Testsuite
=========

To run the testsuite simply run `python setup.py test` which will invoke a Tox
collection testing against various Python and Django versions.

For a specific local installation run `python runtests.py`.

Changelog
=========

v1.0 (in development):
    - Removed some 5 year old dust
    - Django 1.8+ compatible
    - Tests

    Possibly backwards incompatible changes:

    - Removed CreoleParser library in favor of a pypi package
    - The RestructuredText filter now renders level 1 and 2 headers.
      See `Issue 14`_.

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

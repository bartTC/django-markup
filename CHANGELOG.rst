Changelog
=========

v1.2 (2017-03-18):
------------------

- Django 1.10 compatibility and tests.
- Updated all filter dependencies. most notably SmartyPants to v2.0
  which changed it's API, so your project dependencies need to update it
  as well.

v1.1 (2016-05-02):
------------------

- The Markdown filter has the ``safe_mode`` option enabled by default.
- The RestructuredText filter has the file and raw content inclusion
  disabled by default.

v1.0 (2016-01-02):
------------------

- Removed some 5 year old dust
- Django 1.8+ compatible
- Tests

Backwards incompatible changes:

- Removed Pygments highlighting in the Markdown and RestructuredText filter.
- Removed CreoleParser library in favor of a pypi package.
- Removed Lightbox filter.
- The RestructuredText filter now renders level 1 and 2 headers.
  See Github `Issue 14`_ for details and a backwards compatible workaround.

v0.4 (2011-06-01):
------------------

- Added a widont filter
- MarkupField is South compatible.
- Tested with Django 1.3

v0.3 (2009-07-29):
------------------

django-markup now ships with a builtin creole parser. Advantage is, that
the recently used Creoleparser library needs the Genshi lib, which needs
a c-compiler and so on. The builtin creole parser is a pure python library
without any dependencies and follows the wikicreole.org specifications.
django-markup uses the `WikiCreole library`_.

.. _WikiCreole library: http://devel.sheep.art.pl/creole/
.. _Issue 14: https://github.com/bartTC/django-markup/issues/14

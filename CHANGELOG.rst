Changelog
=========

v1.7.2 (2023-05-01):
--------------------

- Fixed a setup.cfg bug that defined the minimal Django version to be v3.7 which does
  not exist. The correct version is 3.2.

v1.7.1 (2023-04-25):
--------------------

- Fixed Python classifiers in setup.cfg.

v1.7 (2023-04-25):
------------------

- Django 4.2 compatibility and tests.
- Python 3.11 compatibility and tests.

v1.6 (2022-08-14):
------------------

- Dropped support for Django <3.2 and Python <3.7.
- Django 3.2 (LTS) compatibility and tests.
- Django 4.0 compatibility and tests.
- Django 4.1 compatibility and tests.
- Python 3.9 compatibility and tests.
- Python 3.10 compatibility and tests.


v1.5 (2020-06-12):
------------------

- Dropped support for Django <=1.11 and Python <=3.5.
- Python 3.8 compatibility and tests.
- Django 3.0 compatibility and tests.
- bleach-whitelist dependency is no longer necessary as tags are now shipped
  with the built-in markdown filter.
- Uses pytest for testing.

v1.4 (2019-03-15):
------------------

- Markdown's safe_mode was deprecated and no longer functional, it's behavior
  was replaced with bleach_.
- Pipfile support for local development and general code cleanup.

.. _bleach: https://github.com/mozilla/bleach

v1.3 (2018-09-07):
------------------

- Python 3.6 and 3.7 compatibility and tests.
- Django 2.0 and 2.1 compatibility and tests.
- The package setup script now provides the ability to install all filter
  dependencies automatically. See the installation Readme for details.

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

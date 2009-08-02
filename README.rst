=============
django-markup
=============

This app is a generic way to provide filters that convert text into html.

The documentation is available with this package in the ``docs/`` folder or
online under this url: http://docs.mahner.org/django-markup/

Changelog
=========

v0.3 (2009-07-29):
    django-markup now ships with a builtin creole parser. Advantage is, that 
    the recently used Creoleparser library needs the Genshi lib, which needs
    a c-compiler and so on. The builtin creole parser is a pure python library
    without any dependencies and follows the wikicreole.org specifications.
    
    django-markup uses the `WikiCreole library`_.
    
.. _WikiCreole library: http://devel.sheep.art.pl/creole/

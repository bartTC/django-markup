.. django-markup documentation master file, created by
   sphinx-quickstart on Mon Jun  1 16:33:50 2009.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-markup's documentation!
=========================================

This app is a generic way to provide filters that convert text into html.
The idea was originally part of the `django-template-utils`_ package by James
Bennet. I've encapsulated the markup system and expanded it into *django-markup*.

.. _`django-template-utils`: http://bitbucket.org/ubernostrum/django-template-utils/

Contents:

.. toctree::
   :maxdepth: 1
   
   installation
   configuration
   filter
   formatter
   usage_python
   usage_templates
   usage_models
  
Bundled filters:
----------------

django-markup comes with a bunch of bundled filters to start right away.
Currently they are:

.. toctree::
   :maxdepth: 1
   :glob:
   
   bundled_filter/*
   
Advanced topic:
---------------

.. toctree::
   :maxdepth: 1
   
   filter_settings
   filter_direct_use
   

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


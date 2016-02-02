============
Installation
============

The easy way:
-------------

Download and install the package from the python package index (pypi)::

    pip install django-markup

Note that `django-markup` ships with some filters ready to use, the
requirements of those filters are not installed by default. If you want to
use all of the filters right away, you can install their latest packages
with::

    pip install textile smartypants docutils markdown python-creole


Install the latest development version
--------------------------------------

The latest development version is available from GitHub. You have to install
git_ and checkout the package with::

    git clone git://github.com/bartTC/django-markup.git

then install it manually::

    cd django-markup
    python setup.py install

Note that the development version is not fully tested and may contain bugs, so
I prefer to use the latest package from pypi.

.. _git: http://git-scm.com/

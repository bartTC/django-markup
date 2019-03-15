============
Installation
============

Download and install the package from the python package index (pypi):

::

    pip install django-markup

Note that `django-markup` ships with some filters ready to use, the
requirements of those filters are not installed by default. If you want to
use all of the filters right away, you can install their latest packages
with:

::

    pip install django-markup[all_filter_dependencies]


Install the latest development version
--------------------------------------

The latest development version is available from GitHub:

::

    git clone git://github.com/bartTC/django-markup.git

Install it with pipenv:

::

    cd django-markup
    pipenv install

Run the testsuite with pipenv as well:

::

    pipenv run ./runtests.py


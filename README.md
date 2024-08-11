<a href="https://pypi.org/project/django-markup/"><img src="https://img.shields.io/pypi/v/django-markup.svg" alt=""/></a> <a href="https://github.com/bartTC/django-markup/actions"><img src="https://github.com/bartTC/django-markup/actions/workflows/push.yml/badge.svg?branch=main" alt=""/></a>

📖 Full documentation on https://django-markup.readthedocs.io/en/latest/

# django-markup

This app is a generic way to provide filters that convert text into html.

## Compatibility Matrix:

| Py/Dj     | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 |
|-----------|-----|-----|------|------|------|
| 3.2 (LTS) | ✓   | ✓   | ✓    | ✓    | ✓    |
| 4.0       | ✓   | ✓   | ✓    | ✓    | ✓    |
| 4.1       | ✓   | ✓   | ✓    | ✓    | ✓    |
| 4.2 (LTS) | ✓   | ✓   | ✓    | ✓    | ✓    |
| 5.0       | —   | —   | ✓    | ✓    | ✓    |
| 5.1       | —   | —   | ✓    | ✓    | ✓    |

## Quickstart

Download and install the package from the python package index (pypi):

Note that `django-markup` ships with some filters ready to use, but the more
complex packages such as Markdown or ReStructuredText are not part of the code.
Please refer the docs which packages are used for the built-in filter.

An alternative is to install django-markup with all filter dependencies
right away. Do so with:

    $ pip install django-markup[all_filter_dependencies]

Then add it to the ``INSTALLED_APPS`` list:

    INSTALLED_APPS = (
        ...
        'django_markup',
    )

Use it in the template:

    {% load markup_tags %}
    {{ the_text|apply_markup:"markdown" }}

Or in Python code:

    from django_markup.markup import formatter
    formatter('Some *Markdown* text.', filter_name='markdown')

# Testsuite

To run the testsuite install the project with pipenv and run it:

    % pipenv install --dev
    $ pipenv run test

You can also test against a variation of Django and Python versions
using tox:

    $ tox


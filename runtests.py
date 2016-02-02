#!/usr/bin/env python
import sys
import os

from django.conf import settings

TESTS_DIR = os.path.join(os.path.dirname(__file__),
                         'src', 'django_markup', 'tests')

SETTINGS = {
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'dev.db',
        },
    },
    'INSTALLED_APPS': [
        'django_markup',
    ],
    'TEMPLATE_DIRS': [
        os.path.join(TESTS_DIR, 'templates')
    ],
}
def runtests(*test_args):
    # Setup settings
    if not settings.configured:
        settings.configure(**SETTINGS)

    # New Django 1.7 app registry setup
    try:
        from django import setup
        setup()
    except ImportError:
        pass

    # New Django 1.8 test runner
    try:
        from django.test.runner import DiscoverRunner as TestRunner
    except ImportError:
        from django.test.simple import DjangoTestSuiteRunner as TestRunner

    test_runner = TestRunner(verbosity=1)
    failures = test_runner.run_tests(['django_markup'])
    if failures:
        sys.exit(failures)

if __name__ == '__main__':
    runtests(*sys.argv[1:])

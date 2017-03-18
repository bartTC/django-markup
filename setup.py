#!/usr/bin/env python
from sys import exit

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errno = tox.cmdline(self.test_args)
        exit(errno)

long_description = u'\n\n'.join((
    open('README.rst').read(),
    open('CHANGELOG.rst').read(),
))

setup(
    name='django-markup',
    version='1.2',
    description='A generic Django application to convert text with specific '
                'markup to html.',
    long_description=long_description,
    author='Martin Mahner',
    author_email='martin@mahner.org',
    url='http://github.com/bartTC/django-markup/',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    package_data={
        'django_markup': ['tests/files/*'],
        'docs': ['*'],
    },
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
    install_requires=[
        'django>=1.4',
        'six',
    ],
    tests_require=[
        'tox>=1.6.1',
    ],
    cmdclass={
        'test': Tox
    },
)

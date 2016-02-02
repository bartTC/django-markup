#!/usr/bin/env python

import os
import importlib.machinery

import setuptools
import pip.req


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
VERSION_FILE_PATH = os.path.join(BASE_DIR, 'src/django_markup/_version.py')
_version = importlib.machinery.SourceFileLoader(
    "django_markup._version", VERSION_FILE_PATH).load_module()

REQUIREMENTS_FILE_PATH = os.path.join(BASE_DIR, 'requirements.pip')
requirements = [str(ir.req) for ir in pip.req.parse_requirements(REQUIREMENTS_FILE_PATH)]


setuptools.setup(
    name='django-markup',
    version=_version.__version__,
    description='A generic Django application to convert text with specific markup to html.',
    long_description=open('README.rst').read(),
    author='Martin Mahner',
    author_email='martin@mahner.org',
    url='http://github.com/bartTC/django-markup/',
    packages=setuptools.find_packages('src'),
    install_requires=requirements,
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    package_data={},
    zip_safe=False,
)

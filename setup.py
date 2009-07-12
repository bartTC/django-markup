from setuptools import setup, find_packages

setup(
    name='django-markup',
    version='0.2',
    description='A generic Django application to convert text with specific markup to html.',
    long_description=open('README.rst').read(),
    author='Martin Mahner',
    author_email='martin@mahner.org',
    url='http://github.com/bartTC/django-markup/tree/master',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    package_data = {},
    zip_safe=False,
)

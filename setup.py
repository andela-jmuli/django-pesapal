#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import django_pesapal

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

version = django_pesapal.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-pesapal',
    version=version,
    description="""A django port of pesapal payment gateway""",
    long_description=readme + '\n\n' + history,
    author='Billy Odero',
    author_email='odero@xx.com',
    url='https://github.com/odero/django-pesapal',
    packages=find_packages(exclude=['sandbox*']),
    package_data={'django_pesapal': ['templates/django_pesapal/*.html']},
    install_requires=[
        'Django>=1.7',
        'oauth2==1.9.0.post1',
        'django-uuidfield<=0.6.0',
        'requests[security]==2.8.1',
    ],
    dependency_links=[
        "https://github.com/dcramer/django-uuidfield/archive/9bd27e9.zip#egg=django-uuidfield-0.6.0",
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-pesapal payment pesapal',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

#!/usr/bin/env python
"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

__author__ = 'Magnus Knutas'
VERSION = '1.1.0'

setup(
    name='aioasuswrt',
    version=VERSION,
    description='Api wrapper for Asuswrt https://www.asus.com/ASUSWRT/',
    setup_requires=['setuptools-markdown'],
    long_description_markdown_filename='README.md',
    url='https://github.com/kennedyshead/aioasuswrt',
    download_url=
    'https://github.com/kennedyshead/aioasuswrt/archive/%s.tar.gz' % VERSION,
    author=__author__,
    author_email='magnusknutas@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='Asuswrt wrapper',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['asyncssh'],
    test_suite='tests',
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage', 'mock'],
    },
)

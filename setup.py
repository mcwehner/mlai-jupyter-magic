#!/usr/bin/env python

from setuptools import setup

with open('VERSION') as fh:
    VERSION = fh.read().strip()

with open('README.md') as fh:
    README = fh.read()

with open('LICENSE') as fh:
    LICENSE = fh.read()

URL = 'https://github.com/mcwehner/mlai-jupyter-magic'

DOWNLOAD_URL = ''

CLASSIFIERS = [
    'Programming Language :: Python',
]

setup(
    name         = 'mlai-jupyter-magic',
    version      = VERSION,
    author       = 'Michael Wehner',
    author_email = '',
    description  = 'IPython magic commands I like having handy',
    license      = LICENSE,
    url          = URL,
    download_url = DOWNLOAD_URL,
    classifiers  = CLASSIFIERS,
    py_modules   = ['mlai_jupyter_magic'],
)

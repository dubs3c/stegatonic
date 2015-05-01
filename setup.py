#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'StegaTonic',
    'author': 'Michael Dubell',
    'url': 'github',
    'download_url': 'http://pypi.python.org/pypi/stegatonic/',
    'author_email': 'michael@mdubell.com',
    'version': '0.5',
    'install_requires': ['Pillow', 'nose', 'argparse'],
    'packages': ['stegatonic'],
    'scripts': [],
    'name': 'StegaTonic'
}

setup(**config)
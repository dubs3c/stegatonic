#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'StegaTonic',
    'author': 'Michael Dubell',
    'url': 'https://github.com/mjdubell/stegatonic',
    'download_url': 'https://github.com/mjdubell/stegatonic',
    'version': '0.5',
    'install_requires': ['Pillow', 'nose', 'argparse','warnings'],
    'packages': ['stegatonic'],
    'scripts': [],
    'name': 'StegaTonic'
}

setup(**config)
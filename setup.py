#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'StegaTonic',
    'description': 'StegaTonic',
    'author': 'Michael Dubell',
    'url': 'https://github.com/mjdubell/stegatonic',
    'download_url': 'https://github.com/mjdubell/stegatonic',
    'version': '1.0',
    'install_requires': ['Pillow', 'nose', 'argparse', 'pycrypto'],
    'packages': ['stegatonic'],
    'scripts': [],
    'license': 'LICENSE.txt'
}

setup(**config)
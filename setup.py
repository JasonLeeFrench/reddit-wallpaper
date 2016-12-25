#!/usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'author': 'Jason French',
    'version': '0.1',
    'packages': ['wallpaper'],
    'name': 'wallpaper',
    'entry_points': {
      'console_scripts': [
        'wallpaper=wallpaper:main'
      ]
    },
    'package_data': {
      'wallpaper': ["secret/user.json"]
    },
    'include_package_data': True
}

setup(**config)

# -*- coding: utf-8 -*-

from setuptools import setup

import gitatat

setup(name = 'gitatat',
      version = gitatat.__version__,
      description = 'wrapper for git commands',
      url = 'https://github.com/vpnagraj/',
      author = 'VP Nagraj',
      author_email = 'vpnagraj@virginia.edu',
      packages = ['gitatat'],
      entry_points = {
          'console_scripts': [
              'gitatat = gitatat.main:main'
          ]
      },
)
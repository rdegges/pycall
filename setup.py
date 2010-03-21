#!/usr/bin/python

"""
setup.py

@author:	Randall Degges
@email:		rdegges@gmail.com
@date:		10-20-09
@license:	GPLv3 (http://www.gnu.org/licenses/gpl-3.0.txt)

This file is used to build, install, and package pycall.
"""

from distutils.core import setup

setup(
	name = 'pycall',
	version = '1.5',
	packages = ['pycall'],
	author = 'Randall Degges',
	author_email = 'rdegges@gmail.com',
	url = 'http://pycall.org/',
	license = 'http://www.gnu.org/licenses/gpl-3.0.txt',
	description = 'A flexible python library for creating and using Asterisk callfiles.',
)


#!/usr/bin/python
"""
	pycall setup
	~~~~~~~~~~~~

	Handles the packaging, distribution, and testing of the pycall library.

	:copyright: (c) 2010 by Randall Degges.
	:license: BSD, see LICENSE for more details.
"""


from setuptools import setup
from setuptools import find_packages


setup(
	name = 'pycall',
	version = '2.0',
	author = 'Randall Degges',
	author_email = 'rdegges@gmail.com',
	packages = ['pycall'],
	url = 'http://pycall.org/',
	license = 'LICENSE',
	description = 'A flexible python library for creating and using Asterisk call files.',
	long_description = open('README').read()
)

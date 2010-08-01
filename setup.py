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

	# Basic package information.
	name = 'pycall',
	version = '2.0',
	packages = find_packages(),

	# Metadata for PyPI.
	author = 'Randall Degges',
	author_email = 'rdegges@gmail.com',
	license = 'BSD',
	url = 'http://pycall.org/',
	keywords = 'asterisk callfile call file telephony voip',
	description = 'A flexible python library for creating and using Asterisk call files.',
	long_description = open('README').read()

)

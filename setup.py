#!/usr/bin/python
"""
	pycall setup
	~~~~~~~~~~~~

	Handles the packaging, distribution, and testing of the pycall library.

	:copyright: (c) 2010 by Randall Degges.
	:license: BSD, see LICENSE for more details.
"""


import ez_setup
ez_setup.use_setuptools()

from setuptools import setup
from setuptools import find_packages


setup(

	# Basic package information.
	name = 'pycall',
	version = '2.0',
	packages = find_packages(),

	# Packaging options.
	include_package_data = True,

	# Package dependencies.
	install_requires = ['coverage>=3.3.1', 'nose>=0.11.4', 'docutils>=0.7'],

	# Metadata for PyPI.
	author = 'Randall Degges',
	author_email = 'rdegges@gmail.com',
	license = 'BSD',
	url = 'http://pycall.org/',
	download_url = 'fillmein',
	keywords = 'asterisk callfile call file telephony voip',
	description = 'A flexible python library for creating and using Asterisk call files.',
	long_description = open('README').read()

)

#!/usr/bin/python
##
# @author	Randall Degges
# @email	rdegges@gmail.com
# @license	BSD (see LICENSE for more information)
#
# This file is used to build, install, and package pycall.
##

from distutils.core import setup

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

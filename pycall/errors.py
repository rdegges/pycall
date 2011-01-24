"""
	pycall.errors
	~~~~~~~~~~~~~

	Implements custom error classes for signaling specific failure conditions
	to developers.

	:copyright: (c) 2010 by Randall Degges.
	:license: BSD, see LICENSE for more details.
"""


from exceptions import Exception


class PycallError(Exception):
	pass

class ValidationError(PycallError):
	def __str__(self): return 'CallFile could not be validated.'

class UnknownError(PycallError):
	def __str__(self): return 'Something must have gone horribly wrong.'

class NoUserPermissionError(PycallError):
	def __str__(self):
		return 'You do not have the appropriate permissions to change ' \
			'ownership of the call file.'

class NoUserError(PycallError):
	def __str__(self):
		return 'No user found. You must specify an actual user in the ' \
			'`user` attribute to change call file ownership to.'

class NoSpoolPermissionError(PycallError):
	def __str__(self):
		return 'You do not have the appropriate permissions to spool the ' \
			'call file.'

#!/usr/bin/python
#
# callfileexceptions.py
#
# @author:	Randall Degges
# @email:	rdegges@gmail.com
# @date:	10-19-09
#
# This file contains all of the custom exceptions defined to help users deal
# with errors in their code.
#
# This file is best viewed in vim. (See .vimrc for more information.)

import exceptions

class NoTrunkTypeDefined(exceptions.Exception):
	"""Exception for use with the CallFile class."""

	def __str__(self):
		print ': No trunk_type was defined!'

class NoTrunkNameDefined(exceptions.Exception):
	"""Exception for use with the CallFile class."""

	def __str__(self):
		print ': No trunk_name was defined!'

class NoNumberDefined(exceptions.Exception):
	"""Exception for use with the CallFile class."""

	def __str__(self):
		print ': No number was defined!'

class NoActionDefined(exceptions.Exception):
	"""Exception for use with the CallFile class."""

	def __str__(self):
		print ': No action was defined! (You must choose either an application or context to execute when the call is answered.)'

class IncorrectTime(exceptions.Exception):
	"""Exception for use with the CallFile class."""

	def __str__(self):
		print ': Incorrect time specified! (The time must be a legitimate datetime object.)'

class NoAsteriskPermission(exceptions.Exception):
	"""Exception for use with the CallFile class."""

	def __str__(self):
		print ': No permissions to send the callfile to Asterisk!'


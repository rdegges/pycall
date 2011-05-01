"""Custom error classes for signaling issues."""


from exceptions import Exception


class PycallError(Exception):
	pass

class InvalidTimeError(PycallError):
	"""You must specify a valid datetime object for the spool method's time
	parameter.
	"""

class NoSpoolPermissionError(PycallError):
	"""You do not have permission to spool this call file."""

class NoUserError(PycallError):
	"""User does not exist."""

class NoUserPermissionError(PycallError):
	"""You do not have permission to change the ownership of this call file."""

class UnknownError(PycallError):
	"""Something must have gone horribly wrong."""

class ValidationError(PycallError):
	"""CallFile could not be validated."""

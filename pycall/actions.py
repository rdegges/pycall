"""A simple wrapper for Asterisk call file actions."""


class Application(object):
	"""Stores and manipulates Asterisk applications and data."""

	def __init__(self, application, data):
		"""Create a new `Application` object.

		:param str application: Asterisk application.
		:param str data: Asterisk application data.
		"""
		self.application = application
		self.data = data


class Context(object):
	"""Stores and manipulates Asterisk contexts, extensions, and priorities."""
	pass

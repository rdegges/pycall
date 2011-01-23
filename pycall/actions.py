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

	def __init__(self, context, extension, priority):
		"""Create a new `Context` object.

		:param str context: Asterisk context to run.
		:param str extension: Asterisk extension to run.
		:param str priority: Asterisk priority to run.
		"""
		self.context = context
		self.extension = extension
		self.priority = priority

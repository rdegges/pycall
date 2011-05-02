"""A simple wrapper for Asterisk call file actions."""


class Action(object):
	"""A generic Asterisk action."""
	pass


class Application(Action):
	"""Stores and manipulates Asterisk applications and data."""

	def __init__(self, application, data):
		"""Create a new `Application` object.

		:param str application: Asterisk application.
		:param str data: Asterisk application data.
		"""
		self.application = application
		self.data = data

	def render(self):
		"""Render this action as call file directives.

		:rtype: Tuple of strings.
		"""
		return ('Application: ' + self.application, 'Data: ' + self.data)


class Context(Action):
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

	def render(self):
		"""Render this action as call file directives.

		:rtype: Tuple of strings.
		"""
		return ('Context: ' + self.context, 'Extension: ' + self.extension,
				'Priority: ' + self.priority)

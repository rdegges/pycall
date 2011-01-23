"""A simple wrapper for Asterisk calls."""


class Call(object):
	"""Stores and manipulates Asterisk calls."""

	def __init__(self, channel, callerid=None, account=None, wait_time=None,
			max_retries=None):
		"""Create a new `Call` object.

		:param str channel: The Asterisk channel to call. Should be in standard
			Asterisk format.
		:param str callerid: CallerID to use.
		:param str account: Account code to associate with this call.
		:param int wait_time: Amount of time to wait (in seconds) between
			retry attempts.
		:param int max_retries: Maximum amount of retry attempts.
		"""
		self.channel = channel
		self.callerid = callerid
		self.account = account
		self.wait_time = wait_time
		self.max_retries = max_retries

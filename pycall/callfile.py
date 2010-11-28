"""A simple wrapper for Asterisk call files."""


from shutil import move
from time import mktime
from pwd import getpwnam
from tempfile import mkstemp
from datetime import datetime
from os import path, chown, utime, fdopen

from errors import *


class CallFile(object):
	"""Stores and manipulates Asterisk call files."""

	#: The default spooling directory (should be OK for most systems).
	DEFAULT_SPOOL_DIR = '/var/spool/asterisk/outgoing'

	def __init__(self, channel, callerid=None, wait_time=None,
			max_retries=None, retry_time=None, account=None, application=None,
			data=None, context=None, extension=None, priority=None,
			set_var=None, archive=None, user=None, tmpdir=None, file_name=None,
			spool_dir=None):
		"""
		Create a new `CallFile` obeject.

		:param str channel:		The number(s) to call. Specified as an \
								Asterisk dial string.
		:param str callerid:	The caller ID to use when making the call.
		:param int wait_time:	Amount of time to wait (in seconds) between \
								retry attempts.
		:param int max_retries:	Maximum amount of times to retry the call if \
								it isn't answered.
		:param int retry_time:	Amount of seconds to wait between retries.
		:param str account:		Account code associated with the call.
		:param str application:	Asterisk application to run upon answer.
		:param str data:		Arguments to application.
		:param str context:		Asterisk context to jump to upon answer.
		:param str extension:	Asterisk extension to jump to upon answer.
		:param str priority:	Asterisk priority to jump to upon answer.
		:param dict set_var:	Variables to pass to Asterisk upon answer.
		:param bool archive:	Should Asterisk archive the call file?
		:param str user:		Username to spool the call file as.
		:param str tmpdir:		Directory to store the temporary call file.
		:param str file_name:	Call file name.
		:param str spool_dir:	Directory to spool the call file to.
		:rtype:					`CallFile` object.
		"""

		if not spool_dir:
			spool_dir = self.DEFAULT_SPOOL_DIR

		args = dict(locals())
		args.pop('self')
		for name, value in args.items():
			setattr(self, name, value)

	def _is_valid(self):
		"""
		Checks all current class attributes to ensure that there are no
		lurking problems.

		:raises:	`NoChannelDefinedError` if no `channel` attribute has \
					been specified.
		:raises:	`NoActionDefinedError` if no action has been specified.
		:rtype:		Boolean.
		"""
		if not self.channel:
			raise NoChannelDefinedError

		if not ((self.application and self.data) or \
			(self.context and self.extension and self.priority)):
			raise NoActionDefinedError

		return True

	def _buildfile(self):
		"""
		Use the class attributes to build a call file string.

		:raises:	`UnknownError` if there were problems validating the call \
					file.
		:returns:	A list consisting of all call file directives.
		:rtype:		List of strings.
		"""
		if not self._is_valid():
			raise UnknownError

		cf = []
		cf.append('Channel: '+self.channel)

		if self.application:
			cf.append('Application: '+self.application)
			cf.append('Data: '+self.data)
		elif self.context and self.extension and self.priority:
			cf.append('Context: '+self.context)
			cf.append('Extension: '+self.extension)
			cf.append('Priority: '+self.priority)
		else:
			raise UnknownError

		if self.set_var:
			for var, value in self.set_var.items():
				cf.append('Set: %s=%s' % (var, value))

		if self.callerid:
			cf.append('Callerid: %s' % self.callerid)

		if self.wait_time:
			cf.append('WaitTime: %s' % self.wait_time)

		if self.max_retries:
			cf.append('Maxretries: %s' % self.max_retries)

		if self.retry_time:
			cf.append('RetryTime: %s' % self.retry_time)

		if self.account:
			cf.append('Account: %s' % self.account)

		if self.archive:
			cf.append('Archive: yes')

		return cf

	def _writefile(self, cf):
		"""
		Write a temporary call file.

		:param cf:	List of call file directives.
		:returns:	Absolute path name of the temporary call file.
		:rtype:		String.
		"""
		if self.tmpdir:
			file, fname = mkstemp(suffix='.call', dir=self.tmpdir)
		else:
			file, fname = mkstemp('.call')

		with fdopen(file, 'w') as f:
			for line in cf:
				f.write(line+'\n')

		return fname

	def spool(self):
		"""Spool the call file with Asterisk."""

		raise NoChannelDefinedError

	def run(self, time=None):
		"""
		Uses the class attributes to submit this `CallFile` to the Asterisk
		spooling directory.

		:param time:	[optional] The time (as a python datetime object) to
						submit this `CallFile` to the Asterisk spooling
						directory.
		:return:		True on success. False on failure.
		"""
		fname = self._writefile(self._buildfile())

		if self.user:
			try:
				pwd = getpwnam(self.user)
				uid = pwd[2]
				gid = pwd[3]

				try:
					chown(fname, uid, gid)
				except:
					raise NoUserPermissionError
			except:
				raise NoUserError

		# Change the modification and access time on the file so that Asterisk
		# knows when to place the call. If time is not specified, then we place
		# the call immediately.
		try:
			time = mktime(time.timetuple())
			utime(fname, (time, time))
		except:
			pass

		try:
			move(fname, self.spool_dir+path.basename(fname))
		except:
			raise NoSpoolPermissionError

		return True

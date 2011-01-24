"""A simple wrapper for Asterisk call files."""


from shutil import move
from time import mktime
from pwd import getpwnam
from tempfile import mkstemp
from os import chown, utime, fdopen

from path import path

from .call import Call
from .actions import Action
from .errors import *


class CallFile(object):
	"""Stores and manipulates Asterisk call files."""

	#: The default spooling directory (should be OK for most systems).
	DEFAULT_SPOOL_DIR = '/var/spool/asterisk/outgoing'

	def __init__(self, call, action, variables=None, archive=None, user=None,
			tmpdir=None, file_name=None, spool_dir=None):
		"""Create a new `CallFile` obeject.

		:param obj call: A `pycall.Call` instance.
		:param obj action: Either a `pycall.actions.Application` instance
			or a `pycall.actions.Context` instance.
		:param dict variables: Variables to pass to Asterisk upon answer.
		:param bool archive: Should Asterisk archive the call file?
		:param str user: Username to spool the call file as.
		:param str tmpdir: Directory to store the temporary call file.
		:param str file_name: Call file name.
		:param str spool_dir: Directory to spool the call file to.
		:rtype: `CallFile` object.
		"""
		self.call = call
		self.action = action
		self.variables = variables
		self.archive = archive
		self.user = user
		self.tmpdir = tmpdir
		self.file_name = file_name
		self.spool_dir = spool_dir or self.DEFAULT_SPOOL_DIR

	def is_valid(self):
		"""Check to see if all `CallFile` attributes are valid.

		:rtype: Boolean.
		"""

		# Fail if `call` isn't a `Call` object.
		if not isinstance(self.call, Call):
			return False

		# Fail if `action` isn't an `Action` subclass.
		if not isinstance(self.action, Action):
			return False

		# Fail if `variables` was specified, but isn't a dictionary.
		if self.variables and not isinstance(self.variables, dict):
			return False

		# Fail if `tmpdir` was specified, but isn't a real directory.
		if self.tmpdir and not path(self.tmpdir).isdir():
			return False

		# Fail if `spool_dir` was specified, but isn't a real directory.
		if self.spool_dir and not path(self.spool_dir).isdir():
			return False

		# Fail if `call` isn't a valid `Call` object.
		if not self.call.is_valid():
			return False

		return True

	def buildfile(self):
		"""Use all attributes to build a call file in memory.

		:raises: `ValidationError` if the `CallFile` could not be validated.
		:returns: A list of all call file directives as they will be written to
			the disk.
		:rtype: List of strings.
		"""
		if not self.is_valid():
			raise ValidationError

		cf = []
		cf += self.call.__str__()
		cf += self.action.__str__()

		if self.variables:
			for var, value in self.variables.items():
				cf.append('Set: %s=%s' % (var, value))

		if self.archive:
			cf.append('Archive: yes')

		return cf

	@property
	def contents(self):
		"""
		Get the contents of this call file.

		:returns: Call file contents.
		:rtype: String.
		"""
		return '\n'.join(self.buildfile())

	def writefile(self):
		"""
		Write a temporary call file to disk.

		:returns: Absolute path name of the temporary call file.
		:rtype: String.
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

		raise NoActionDefinedError

	def run(self, time=None):
		"""
		Uses the class attributes to submit this `CallFile` to the Asterisk
		spooling directory.

		:param datetime time: [optional] The date and time to spool this call
			file.
		:rtype: Boolean.
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

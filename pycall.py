#!/usr/bin/python
"""
	pycall
	~~~~~~

	A flexible python library for creating and using Asterisk call files.

	:copyright: (c) 2010 by Randall Degges.
	:license: BSD, see LICENSE for more details.

	This file contains the entire pycall library source code.
"""


from shutil import move
from time import mktime
from pwd import getpwnam
from tempfile import mkstemp
from datetime import datetime
from exceptions import Exception
from os import path, chown, utime, fdopen


class PycallError(Exception):
	pass

class UnknownError(PycallError):
	def __str__(self): return 'Something must have gone horribly wrong.'

class NoChannelDefinedError(PycallError):
	def __str__(self):
		return 'You must define either the `channel` attribute or the ' \
			'`trunk_type`, `trunk_name`, and `number` attributes.'


class CallFile:
	"""
	Stores and manipulates call file information. Also allows users to schedule
	call files to be spooled.
	"""

	def __init__(
		self, channel=None, trunk_type=None, trunk_name=None, number=None,
		callerid=None, callerid_name=None, callerid_num=None, wait_time=None,
		max_retries=None, retry_time=None, account=None, application=None,
		data=None, context=None, extension=None, priority=None, set_var=None,
		archive=None, user=None, tmpdir=None,
		spool_dir='/var/spool/asterisk/outgoing/'
	):

		args = dict(locals())
		args.pop('self')
		for name, value in args.items():
			setattr(self, name, value)

	def add_set(self, var, val):
		"""
		Add a variable / value definition to the callfile to pass to Asterisk.
		"""

		self.sets[var] = val

	def __is_valid(self):
		"""
		Checks all current class attributes to ensure that there are no
		lurking problems.

		:returns:	True if no problems. False if problems. May raise
					exceptions if necessary.
		"""
		pass

	def __buildfile(self):
		"""
		Use the class attributes to build a call file string.

		:return:	A call file string, ready to be spooled.
		"""
		if not __is_valid():
			raise UnknownError

		# Make sure the user has defined a trunk type, trunk name, and number
		# to call. This is required for every callfile.
		if not self.trunk_type:
			raise NoTrunkTypeDefined
		if not self.trunk_name:
			raise NoTrunkNameDefined
		if not self.number:
			raise NoNumberDefined

		# Make sure the user has defined either an application or a context
		# (some action to perform if the call is answered). This is required
		# for every call file.
		if (not self.application or not self.data) and (not self.context or not self.extension or not self.priority):
			raise NoActionDefined

		# Start building the callfile list. Each list element is a line in the
		# call file.
		callfile = []
		if self.trunk_type.lower() == 'local':
			callfile.append('Channel: %s/%s@%s' % (self.trunk_type, self.number, self.trunk_name))
		else:
			callfile.append('Channel: %s/%s/%s' % (self.trunk_type, self.trunk_name, self.number))

		# If CallerID was specified, then use it.
		callerid = ''
		if self.callerid_name:
			callerid += '"%s" ' % self.callerid_name
		if self.callerid_num:
			callerid += '<%s>' % self.callerid_num
		if callerid:
			callfile.append('CallerID: %s' % callerid)

		# If MaxRetries was specified, then use it.
		if self.max_retries:
			callfile.append('MaxRetries: %s' % self.max_retries)

		# If RetryTime was specified, then use it.
		if self.retry_time:
			callfile.append('RetryTime: %s' % self.retry_time)

		# If WaitTime was specified, then use it.
		if self.wait_time:
			callfile.append('WaitTime: %s' % self.wait_time)

		# If Account was specified, then use it.
		if self.account:
			callfile.append('Account: %s' % self.account)

		# Add in the application / context depending on what was specified.
		if self.application:
			callfile.append('Application: %s' % self.application)
			callfile.append('Data: %s' % self.data)
		else:
			callfile.append('Context: %s' % self.context)
			callfile.append('Extension: %s' % self.extension)
			callfile.append('Priority: %s' % self.priority)

		# If there are any variables to pass to Asterisk, add them.
		for var, value in self.sets.iteritems():
			callfile.append('Set: %s=%s' % (var, str(value)))

		# Set AlwaysDelete appropriately.
		if self.always_delete:
			callfile.append('AlwaysDelete: Yes')
		else:
			callfile.append('AlwaysDelete: No')

		# Set the Archive appropriately.
		if self.archive:
			callfile.append('Archive: Yes')
		else:
			callfile.append('Archive: No')

		return callfile

	def writefile(self, callfile):
		"""
		Given a callfile list to write, writes the actual callfile and returns the absolute
		name of the file written. DOES NOT DELETE THE CREATED FILE.
		"""

		# Securely request a .call file from the OS.
		if self.tmpdir:
			file, fname = mkstemp(suffix = '.call', dir = self.tmpdir)
		else:
			file, fname = mkstemp('.call')

		# Open the file and write it, then close the file.
		f = fdopen(file, 'w')
		for line in callfile:
			f.write(line + '\n')
		f.close()

		return fname

	def run(self, time=None):
		"""
		Uses the class attributes to submit this `CallFile` to the Asterisk
		spooling directory.

		:param time:	[optional] The time (as a python datetime object) to
						submit this `CallFile` to the Asterisk spooling
						directory.
		"""

		# Build the file from our settings, then write the file, and store the
		# written file name.
		fname = self.writefile(self.buildfile())

		# If user is specified, chown the file to the appropriate user.
		if self.user:
			try:
				pwd = getpwnam(self.user)
				uid = pwd[2]
				gid = pwd[3]

				try:
					chown(fname, uid, gid)
				except:
					NoPermissionException
			except:
				raise NoUserException

		# Change the modification time on the file (access time too) so that
		# Asterisk knows when to place the call. If none is specified, then we
		# place the call immediately.
		try:
			time = mktime(time.timetuple())
			utime(fname, (time, time))
		except:
			utime(fname, None)

		# Move the file to asterisk (hand over control).
		try:
			move(fname, self.dir + path.basename(fname))
		except:
			raise NoAsteriskPermission

if __name__ == '__main__':

	print 'You have pycall installed. Check out our website for more' \
		'information, http://pycall.org/'

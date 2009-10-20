#!/usr/bin/python
#
# callfile.py
#
# @author:	Randall Degges
# @email:	rdegges@gmail.com
# @date:	10-19-09
#
# This is the CallFile class which can be used to create / use / handle Asterisk
# callfiles simply. The class automatically handles all file operations.
#
# This file is best viewed in vim. (See .vimrc for more information.)

from tempfile import mkstemp
from datetime import datetime
from callfileexceptions import *

class CallFile:
	"""This class allows you to create and use Asterisk callfiles simply."""

	def __init__(self, time='', trunk_type='', trunk_name='', number='', callerid_name='', callerid_num='', max_retries=0, retry_time=0, wait_time=0, account='', context='', extension='', priority='', application='', data='', sets={}, always_delete=False, archive=False):

		self.file, self.fname = mkstemp('.call')
		self.time = time
		self.trunk_type = trunk_type
		self.trunk_name = trunk_name
		self.number = number
		self.callerid_name = callerid_name
		self.callerid_num = callerid_num
		self.max_retries = max_retries
		self.retry_time = retry_time
		self.wait_time = wait_time
		self.account = account
		self.context = context
		self.extension = extension
		self.priority = priority
		self.application = application
		self.data = data
		self.sets = sets
		self.always_delete = always_delete
		self.archive = archive

		print locals().keys()

	def add_set(self, var, val):
		"""Add a variable / value definition to the callfile to pass to Asterisk."""

		self.sets[var] = val

	def buildfile(self):
		"""Use the settings in memory to build a callfile string."""

		# Make sure the user has defined a trunk type, trunk name, and number to
		# call. This is required for every callfile.
		if not self.trunk_type:
			raise NoTrunkTypeDefined
		if not self.trunk_name:
			raise NoTrunkNameDefined
		if not self.number:
			raise NoNumberDefined

		# Make sure the user has defined either an application or a context
		# (some action to perform if the call is answered). This is required for
		# every callfile.
		if (not self.application or not self.data) and (not self.context or not self.extension or not self.priority):
			raise NoActionDefined

		# Start building the callfile list. Each list element is a line in the
		# callfile.
		callfile = []
		callfile.append('Channel: %s/%s/%s' % (self.trunk_type, self.trunk_name, self.number))

		# If CallerID was specified, then use it.
		callerid = ''
		if self.callerid_name:
			callerid += '"%s" ' % self.callerid_name
		if self.callerid_num:
			callerid += '<%s>' % se;f.callerid_num
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
			callfile.append('Set: %s=%s' % (var, value))

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

#	# Write out the CallFile using the settings in memory.
#	def writefile(self):
#
#		f = fdopen(self.file, 'w')
#		f.write(buildfile())
#		f.close()

#	# Schedule the CallFile with Asterisk.
#	def run(self, time=datetime.now()):
#
#		# Write the file.
#		_writefile(
#
#		# Set the timestamp on the file (so Asterisk knows when to place the
#		# call).
#		utime(self.fname, (x, 



# Used for testing.
if __name__ == '__main__':
	callfile = CallFile()

	callfile.trunk_type = 'SIP'
	callfile.trunk_name = 'flowroute'
	callfile.number = '18182179229'
	callfile.application = 'Playback'
	callfile.data = 'hello-world'
	#callfile.context = 'do_something'
	#callfile.extension = 's'
	#callfile.priority = '1'

	print "\nCallFile:\n"
	print callfile.buildfile()

#	try:
#		raise NoTrunkTypeDefined
#	except NoTrunkTypeDefined:
#		print 'fuck'

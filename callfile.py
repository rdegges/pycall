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

	def __init__(self, time='', trunk_type='', trunk_name='', number='', callerid='', callerid_name='', callerid_num='', max_retries=0, retry_time=0, wait_time=45, account='', context='', extension='', priority='', application='', data='', sets=[], always_delete=False, archive=False):

		self.file, self.fname = mkstemp('.call')
		self.time = time
		self.trunk_type = trunk_type
		self.trunk_name = trunk_name
		self.number = number
		self.callerid = callerid
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

	# All functions below allow the user to set / update / override callfile
	# settings.
	# ====================
	def set_trunk_type(self, trunk_type):
		self.trunk_type = trunk_type
	def set_trunk_name(self, trunk_name):
		self.trunk_name = trunk_name
	def set_number(self, number):
		self.number = number
	def set_callerid(self, callerid):
		self.callerid = callerid
	def set_callerid_name(self, callerid_name):
		self.callerid_name = callerid_name
	def set_callerid_num(self, callerid_num):
		self.callerid_num = callerid_num
	def set_max_retries(self, max_retries):
		self.max_retries = max_retries
	def set_retry_time(self, retry_time):
		self.retry_time = retry_time
	def set_wait_time(self, wait_time):
		self.wait_time = wait_time
	def set_account(self, account):
		self.account = account
	def set_context(self, context):
		self.context = context
	def set_extension(self, extension):
		self.extension = extension
	def set_priority(self, priority):
		self.priority = priority
	def set_application(self, application):
		self.application = application
	def set_data(self, data):
		self.data = data
	def set_set(self, var, val):
		self.sets.append("%s=%s" % (var, val))
	def set_always_delete(self, always_delete):
		self.always_delete = always_delete
	def set_archive(self, archive):
		self.archive = archive
	# ====================

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
		if not self.application and (not self.context or not self.extension or not self.priority):
			raise NoActionDefined

		

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
	callfile.buildfile()

#	try:
#		raise NoTrunkTypeDefined
#	except NoTrunkTypeDefined:
#		print 'fuck'

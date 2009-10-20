#!/usr/bin/python
#
# run-as-user.py
#
# @author:	Randall Degges
# @email:	rdegges@gmail.com
# @date:	10-20-09
# @license:	GPLv3 (http://www.gnu.org/licenses/gpl-3.0.txt)
#
# This sample program demonstrates how to force the callfile to run as another
# user. This is useful on systems where Asterisk can only read callfiles that
# are created by a particular user. This is the same as chown'ing a callfile to
# a certain user before sending it off to Asterisk.

from pycall.callfile import *
from pycall.callfileexceptions import *

def main():

	# Define our callfile.
	callfile = CallFile(
		trunk_type = 'SIP',
		trunk_name = 'flowroute',
		number = '12223334444',
		application = 'Playback',
		data = 'hello-world',
		user = 'asterisk'			# chown the callfile to user 'asterisk'.
	)

	# Create / run the callfile as user 'asterisk'. Always use try / except
	# when specifying a user to catch errors. If the user specified does not
	# exist on the system, a NoUserException is raised. If we do not have
	# permissions to chown the file to the specified user, then a
	# NoPermissionException is raised.
	try:
		callfile.run()
	except NoUserException:
		print "User %s doesn't exist. Skipping call." % callfile.user
	except NoPermissionException:
		print "We do not have the permissions to change ownership of the callfile to user %s. Skipping the call." % callfile.user

	# Change ownership of the callfile to user 'nobody' and then run the
	# callfile. Wrap the statement in a try / except to catch errors.
	callfile.user = 'nobody'
	try:
		callfile.run()
	except NoUserException:
		print "User %s doesn't exist. Skipping call." % callfile.user
	except NoPermissionException:
		print "We do not have the permissions to change ownership of the callfile to user %s. SKipping the call." % callfile.user

if __name__ == '__main__':
	main()

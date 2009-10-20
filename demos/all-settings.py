#!/usr/bin/python
#
# all-settings.py
#
# @author:	Randall Degges
# @email:	rdegges@gmail.com
# @date:	10-20-09
# @license:	GPLv3 (http://www.gnu.org/licenses/gpl-3.0.txt)
#
# This sample program demonstrates how to create a callfile using ALL of the
# options. It doens't do any error checking (so you may get errors if you put in
# invalid information), but it does show all of the options and how to use them.

from pycall.callfile import *
from pycall.callfileexceptions import *

def main():

	# Define our callfile.
	callfile = CallFile(
		trunk_type = 'SIP',
		trunk_name = 'flowroute',
		number = '12223334444',
		max_retries = 10,	# Try the call 10 times if nobody picks up.
		retry_time = 30,	# Wait 30 seconds before each retry.
		wait_time = 60,		# Wait 60 seconds for the person to pick up.
		account = '1000',	# Log all calls under the account '1000' for CDR.
		application = 'Playback',	# When the user picks up do a Playback.
		data = 'hello-world',		# Play the soundfile hello-world.
		sets = {'fun': 'yes', 'hi': 'there'},
		always_delete = True,		# Delete the file if it is scheduled to run.
		archive = True,		# Archive finished files.
		user = 'nobody'		# Run the callfile as user 'nobody'.
	)

	# The sets (defined above) lets us pass variables and their values to
	# Asterisk when our call is answered. This is covered in depth in the
	# variable-passing.py demo.

	# Run the call.
	callfile.run()

if __name__ == '__main__':
	main()

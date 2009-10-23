#!/usr/bin/python
#
# variable-passing.py
#
# @author:	Randall Degges
# @email:	rdegges@gmail.com
# @date:	10-22-09
# @license:	GPLv3 (http://www.gnu.org/licenses/gpl-3.0.txt)
#
# This sample program demonstrates how to create a callfile which sets certain
# variables--alerting Asterisk of their values. This is useful when you need to
# create a call file, but also need to pass Asterisk certain information that it
# can use once the call is answered. The following example creates a call file
# and sets several variables which give Asterisk information about the person we
# are calling.

from pycall.callfile import *
from pycall.callfileexceptions import *

def main():

	# Define our callfile.
	callfile = CallFile(
		trunk_type = 'SIP',
		trunk_name = 'flowroute',
		number = '12223334444',
		application = 'Playback',	# When the user picks up do a Playback.
		data = 'hello-world',		# Play the soundfile hello-world.
		sets = {'name': 'Randall Degges',
			'phonenum': '18182223333',
			'height': '6"0',
			'pets': 3,
			'girlfriend': True,
		},
	)

	# To pass variables to Asterisk, simply build a dictionary and pass it as
	# the sets variable.

	# Run the call.
	callfile.run()

if __name__ == '__main__':
	main()

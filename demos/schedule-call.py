#!/usr/bin/python
#
# schedule-call.py
#
# @author:	Randall Degges
# @email:	rdegges@gmail.com
# @date:	10-20-09
# @license:	GPLv3 (http://www.gnu.org/licenses/gpl-3.0.txt)
#
# This sample program demonstrates how to schedule calls in the future using the
# pycall library. It is easy and intuitive. This example schedules calls in the
# future in several ways. Read the source for more information.
#
# Each call is placed to the number 1-555-444-3333 and goes out of the flowroute
# SIP trunk. Once the call is answered it plays the hello-world soundfile and
# hangs up (to keep the example simple).

from datetime import datetime
from pycall.callfile import *
from pycall.callfileexceptions import *

def main():

	# Define our callfile.
	callfile = CallFile(
		trunk_type = 'SIP',
		trunk_name = 'flowroute',
		number = '15554443333',
		application = 'Playback',
		data = 'hello-world'
	)

	# Get the current time and add 1 hour to it. This is the time we want to
	# schedule the call at.
	time = datetime.now()
	time = datetime(time.year, time.month, time.day, time.hour+1, time.minute, time.second)

	# Place the call in 1 hour.
	callfile.run(time)

	# Create a datetime object to schedule a call on December 1, 2010 at 1:00am.
	time = datetime(2010, 12, 1, 1, 0, 0)

	# Hand the call over to Asterisk (won't run until December 1, 2010 at 1:00am
	# !)
	callfile.run(time)

	# Place the next call immediately. As you can see, if you want the call to
	# be placed immediately, you don't need to specify any time stuff.
	callfile.run()

	# This example shows an error. We purposely try specify an invalid time for
	# the call to run (we don't even create a datetime object, we just randomly
	# pass a number. As you will see, if this happens, pycall ignores your
	# mistake and places the call immediately. No errors are raised.
	callfile.run(100)

if __name__ == '__main__':
	main()

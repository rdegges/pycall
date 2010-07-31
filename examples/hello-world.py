#!/usr/bin/python

"""
hello-world.py

@author:	Randall Degges
@email:	rdegges@gmail.com
@date:	10-20-09
@license:	GPLv3 (http://www.gnu.org/licenses/gpl-3.0.txt)

This sample program creates a minimal callfile which dials the number 1-800-222-3333 out of
the DAHDI/g0 trunk. Once the call has been answered, the system plays the hello-world sound
file, then hangs up.
"""

from pycall.callfile import *
from pycall.callfileexceptions import *

def main():

	callfile = CallFile(
		trunk_type = 'DAHDI',
		trunk_name = 'g0',
		number = '18002223333',
		application = 'Playback',
		data = 'hello-world'
	)

	# Place the call now.
	callfile.run()

if __name__ == '__main__':
	main()

#!/usr/bin/python

#import pycall.callfile
from pycall.callfile import *
from pycall.callfileexceptions import *

if __name__ == '__main__':
	callfile = CallFile()
	callfile.trunk_type = 'SIP'
	callfile.trunk_name = 'flowroute'

	print callfile.trunk_name
	callfile.run()

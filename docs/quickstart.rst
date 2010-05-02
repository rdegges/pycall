.. _quickstart:

Quickstart
==========

Eager to get started? This page gives a good introduction to pycall. This doc
assumes you already have pycall installed. If not, head over to the
:ref:`installation` section.

Preparation
-----------

Before getting started with the rest of this quickstart, a few things must be
ready and working.

1.	Your Asterisk server should be up and running. If you don't have Asterisk
	installed and working, you can read some of my blog posts which explain (in
	detail) how to install and configure Asterisk:

	*	`Installing Asterisk <http://projectb14ck.org/2010/02/28/transparent-telephony-part-2-installing-asterisk/>`_
	*	`Making and Receiving Calls Using VoIP <http://projectb14ck.org/2010/03/03/transparent-telephony-part-3-making-your-first-call/>`_

2.	You should have some sort of PSTN (public switch telephone network)
	connectivity configured and ready to go. Regardless of what sort of PSTN
	connection you have (SIP / DAHDI / ZAPTEL / ISDN / etc.), as long as you
	can	make calls, you're fine.

A Minimal Application
---------------------

A minimal pycall application looks something like this::

	import sys
	from pycall.callfile import CallFile

	def call(number):
		cf = CallFile(
			trunk_type = 'Local',
			trunk_name = 'from-internal',
			number = number,
			application = 'Playback',
			data = 'hello-world'
		)
		cf.run()

	if __name__ == '__main__':
		call(sys.argv[1])

Just save it as `hello.py` or something similar, and run it with your Python
interpreter. ::

	$ python hello.py 18002223333

Now if all is working, your phone should be getting a call, and once you pick
up the call, you should hear Asterisk say 'hello world' then hang up the call.

So what did the code do?

1.	First we imported the :class:`~callfile.CallFile` class. An instance of
	this class holds all relative Asterisk information needed to generate a
	valid call file object.

2.	Next, we create an instance of it. We pass it the trunk type that our
	Asterisk system uses (`Local` is a safe default), and the trunk name
	(`from-internal` is a safe default). We then specify the number to call.
	Lastly, we choose an Asterisk application to execute once the call has been
	answered, and provide data to the application.

3.	We submit the call file to the Asterisk spooler by calling the
	:meth:`~callfile.CallFile.run` method to tell pycall to generate the call
	file and make the call instantly.

Pretty simple right?

Scheduling a Call in the Future
-------------------------------

Now that we've gotten a simple pycall program working, let's take our hello
example a bit further, and schedule the call to run at some point in the
future. 

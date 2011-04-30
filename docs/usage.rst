.. _usage:

Usage
=====

Integrating pycall into your project is quick and easy! After reading through
the sections below, you should be able to integrate pycall into your project,
and understand what it can and cannot be used for.

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

In addition to providing an extremely easy way to initiate call files (as we
saw in the previous section, pycall also supports timed call file initiation.

Put simply: pycall allows you to specify a time to run the call file. Let's
take a look at a short example. In this example, we'll have pycall schedule our
call file to launch precisely one hour from now: ::

	import sys
	from datetime import datetime
	from datetime import timedelta
	from pycall.callfile import CallFile

	def call(number, time=None):
		cf = CallFile(
			trunk_type = 'Local',
			trunk_name = 'from-internal',
			number = number,
			application = 'Playback',
			data = 'hello-world'
		)
		cf.run(time)

	if __name__ == '__main__':
		call(sys.argv[1], datetime.now()+timedelta(hours=1))

What did we change? Not much. The :meth:`~callfile.CallFile.run` method
supports an optional datetime argument which can be used to specify at which
time Asterisk should actually run the call file.

What pycall actually does if the *time* argument is supplied is set the call
file's modification time and access time so that the Asterisk spooling daemon
will leave the call file in the Asterisk spooling directory until the system
time reaches the modification time.

Just for the heck of it, let's look at one more code snippet. This time we'll
tell Asterisk to run the call file at exactly 1:00 AM on December 1, 2010. ::

	import sys
	from datetime import datetime
	from pycall.callfile import CallFile

	def call(number, time=None):
		cf = CallFile(
			trunk_type = 'Local',
			trunk_name = 'from-internal',
			number = number,
			application = 'Playback',
			data = 'hello-world'
		)
		cf.run(time)

	if __name__ == '__main__':
		call(sys.argv[1], datetime(2010, 12, 1, 1, 0, 0))

Scheduling calls is a piece of cake!

How to Run Call Files Under Another User
----------------------------------------

One problem we often face as programmers is getting proper permissions on our
running code. With Asterisk, and call files, this can be especially tricky as
the Asterisk spooling daemon will only read call files that is has permission
to read.

In most environments, Asterisk is installed and ran as the user / group
'asterisk', which poses a problem, as your code will surely not be running as
the 'asterisk' user. If by chance your Asterisk install doesn't run as the
'asterisk' user, then feel free to make mental substitutions as necessary.

pycall recognizes that this is a frustrating problem to deal with, and provides
three mechanisms for helping make permissions as painless as possible: the
:attr:`~callfile.CallFile.user` attribute, the
:class:`~callfileexceptions.NoUserException` exception, and the
:class:`~callfileexceptions.NoPermissionException` exception.

The :attr:`~callfile.CallFile.user` attribute is used to speciy the user
account that your call file should be ran as. The
:class:`~callfileexceptions.NoUserException` exception will be raised in your
code if the user attribute you specify doesn't exist on the system, and the
:class:`~callfileexceptions.NoPermissionException` exception will be raised if
you specify a user account in your user attribute that your running user
account doesn't have permission to change file ownership for.

To help understand why pycall provides these mechanisms, let's use our
imagination. All scenarios below are based on the following code: ::

	from sys import argv
	from pycall.callfile import CallFile
	from pycall.callfileexceptions import NoUserException
	from pycall.callfileexceptions import NoPermissionException

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
		call(argv[1])

**Scenario 1 - Not Sure Which User Asterisk Runs As**

In this scenario, we're developing an application using pycall, but we aren't
really sure which user Asterisk is configured to run as. In this situation, we
first try running the code above exactly as-is, but we notice that the Asterisk
spooling daemon never runs our call file.

Next, we try setting the :attr:`~callfile.CallFile.user` attribute to run the
call file as the user asterisk: ::

	cf = CallFile(
		trunk_type = 'Local',
		trunk_name = 'from-internal',
		number = number,
		application = 'Playback',
		data = 'hello-world',
		user = 'asterisk'
	)
	cf.run()

And bam! It magically works. Now we know that Asterisk is running as the user
asterisk on our system, so pycall fixed all problems for us.

**Scenario 2 - We Don't Have Permissions to


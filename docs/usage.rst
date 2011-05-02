.. _usage:

Usage
=====

Integrating pycall into your project is quick and easy! After reading through
the sections below, you should be able to integrate pycall into your project,
and understand what it can and cannot be used for.


Preparation
-----------

The rest of this guide assumes you have the following:

1.	A working Asterisk server.

2.	Some sort of PSTN (public switch telephone network) connectivity.
	Regardless of what sort of PSTN connection you have (SIP / DAHDI / ZAPTEL /
	ISDN / etc.), as long as you can make calls, you're fine.

For simplicity's sake, I'm going to assume for the rest of this guide that you
have a SIP trunk named `flowroute` defined.


Hello, World!
-------------

pycall allows you to build applications that automate outbound calling. In the
example below, we'll call a phone number specified on the command line, say
"hello world", then hang up! ::

	import sys
	from pycall import CallFile, Call, Application

	def call(number):
		c = Call('SIP/flowroute/%s' % number)
		a = Application('Playback', 'hello-world')
		cf = CallFile(c, a)
		cf.spool()

	if __name__ == '__main__':
		call(sys.argv[1])

Just save the code above in a file named `call.py` and run it with python! ::

	$ python call.py 18002223333

Assuming your Asterisk server is setup correctly, your program just placed a
call to the phone number `18002223333`, and said "hello world" to the person
who answered the phone!

Code Breakdown
**************

1.	First we imported the pycall classes. The :class:`~pycall.CallFile` class
	allows us to make call files. The :class:`~pycall.Call` class stores
	information about a specific call, and the :class:`~pycall.Application`
	class lets us specify an Asterisk application as our
	:class:`~pycall.Action`.  Every call file requires some sort of action
	(what do you want to do when the caller answers?).

2.	Next, we build a :class:`~pycall.Call` object, and specify the phone number
	to call in `standard Asterisk format
	<http://www.voip-info.org/wiki/view/Asterisk+cmd+Dial>`_. This tells
	Asterisk who to call.

.. note::

   In this example we made a call out of a SIP trunk named `flowroute`, but you
   can specify any sort of dial string in its place. You can even tell Asterisk
   to call multiple phone numbers at once by separating your dial strings with
   the & character (eg: `Local/1000@internal&SIP/flowroute/18002223333`).

3.	Then we build an :class:`~pycall.Application` object that tells Asterisk
	what to do when the caller answers our call. In this case, we tell Asterisk
	to run the `Playback
	<http://www.voip-info.org/wiki/view/Asterisk+cmd+Playback>`_ command, and
	pass the argument 'hello-world' to it.

.. note::

	The name 'hello-world' here refers to one of the default Asterisk sound
	files that comes with all Asterisk installations. This file can be found in
	the directory `/var/lib/asterisk/sounds/en/` on most systems.

4.	Finally, we create the actual :class:`~pycall.CallFile` object, and run
	its :meth:`~pycall.CallFile.spool` method to have Asterisk make the call.


Scheduling a Call in the Future
-------------------------------

Let's say you want to have Asterisk make a call at a certain time in the
future--no problem. The :meth:`~pycall.CallFile.spool` method allows you to
specify an optional datetime object to tell Asterisk when you want the magic to
happen.

In this example, we'll tell Asterisk to run the call in exactly 1 hour: ::

	import sys
	from datetime import datetime
	from datetime import timedelta
	from pycall import CallFile, Call, Application

	def call(number, time=None):
		c = Call('SIP/flowroute/%s' % number)
		a = Application('Playback', 'hello-world')
		cf = CallFile(c, a)
		cf.spool(time)

	if __name__ == '__main__':
		call(sys.argv[1], datetime.now()+timedelta(hours=1))

.. note::

	If you specify a value of `None`, the call file will be ran immediately.

Just for the heck of it, let's look at one more code snippet. This time we'll
tell Asterisk to run the call file at exactly 1:00 AM on December 1, 2010. ::

	import sys
	from datetime import datetime
	from pycall.callfile import CallFile

	def call(number, time=None):
		c = Call('SIP/flowroute/%s' % number)
		a = Application('Playback', 'hello-world')
		cf = CallFile(c, a)
		cf.spool(time)

	if __name__ == '__main__':
		call(sys.argv[1], datetime(2010, 12, 1, 1, 0, 0))


Setting Call File Permissions
-----------------------------

In most environments, Asterisk is installed and ran as the user / group
'asterisk', which often poses a problem if your application doesn't run under
the 'asterisk' user account.

pycall recognizes that this is a frustrating problem to deal with, and provides
three mechanisms for helping make permissions as painless as possible: the
:attr:`~pycall.CallFile.user` attribute, the
:class:`~pycall.errors.NoUserError`, and the
:class:`~pycall.errors.NoUserPermissionError`.

*	The :attr:`~pycall.CallFile.user` attribute lets you specify a system
	username that your call file should be ran as. For example, if your
	application is running as 'root', you could say::

		cf = CallFile(c, a, user='asterisk')

	and pycall would chown the call file to the 'asterisk' user before
	spooling.

*	If you specify the :attr:`~pycall.CallFile.user` attribute, but the user
	doesn't exist, pycall will raise the :class:`~pycall.errors.NoUserError` so
	you know what's wrong.

*	Lastly, if your application doesn't have the proper permissions to change
	the ownership of your call file, pycall will raise the
	:class:`~pycall.errors.NoUserPermissionError`.

As an example, here we'll change the call file permissions so that Asterisk can
actually read our call file: ::

	import sys
	from pycall import CallFile, Call, Application

	def call(number):
		c = Call('SIP/flowroute/%s' % number)
		a = Application('Playback', 'hello-world')
		cf = CallFile(c, a, user='asterisk')
		cf.spool(time)

	if __name__ == '__main__':
		call(sys.argv[1])

.. note::

	If you run this code on a system that doesn't have Asterisk installed, you
	will most likely get a :class:`~pycall.errors.NoUserError` since pycall
	won't be able to find the 'asterisk' user that it's trying to grant
	permissions to.


Adding Complex Call Logic
-------------------------

Most applications you write will probably be a bit more complex than "hello
world". In the example below, we'll harness the power of the
:class:`~pycall.Context` class to instruct Asterisk to run some custom
`dial plan <http://www.voip-info.org/tiki-index.php?page=Asterisk%20config%20extensions.conf>`_
code after the caller answers. ::

	from pycall import CallFile, Call, Context

	c = Call('SIP/flowroute/18002223333')
	con = Context('survey', 's', '1')
	cf = CallFile(c, con)
	cf.spool()

For example purposes, let's assume that somewhere in your Asterisk
`extensions.conf` file there exists some dial plan in a context labeled
`survey`.

After the caller answers our call, Asterisk will immediately jump to the dial
plan code we've specified at `survey,s,1` and start executing as much logic as
desired.


Setting a CallerID
------------------

A lot of the time, you'll want to force Asterisk to assume a specific caller ID
when making outbound calls. To do this, simply specify a value for the
:attr:`~pycall.Call.callerid` attribute: ::

	c = Call('SIP/flowroute/18002223333', callerid="'Test User' <5555555555>'")

Now, when Asterisk makes your call, the person receiving the call (depending on
their phone and service type) should see a call coming from "Test User" who's
phone number is 555-555-5555!


Passing Variables to Your Dial Plan
-----------------------------------

Often times, when building complex applications, you'll want to pass specific
data from your application to Asterisk, so that you can read the information
later.

The example below will pass some information to our Asterisk dial plan code, so
that it can use the information in our call. ::

	from pycall import CallFile, Call, Context

	vars = {'greeting': 'tt-monkeys'}

	c = Call('SIP/flowroute/18882223333', variables=vars)
	x = Context('survey', 's', '1')
	cf = CallFile(c, x)
	cf.spool()

And somewhere in our `extensions.conf` file... ::

	[survey]
	exten => s,1,Playback(${greeting})
	exten => s,n,Hangup()

As you can see, our dial plan code can now access the variable 'greeting' and
its value.


Track Your Calls with Asterisk Account Codes
--------------------------------------------

Asterisk call files allow you to specify that a certain call should be
associated with a certain account. This is mainly useful for logging purposes.
This example logs the call with the 'randall' account: ::

	c = Call('SIP/flowroute/18002223333', account='randall')

.. note::

	For more information on call logs, read the `CDR documentation
	<http://www.voip-info.org/wiki/view/Asterisk+cdr+csv>`_.


Specify Call Timing Values
--------------------------

pycall provides several ways to control the timing of your calls.

1.	:attr:`~pycall.Call.wait_time` lets you specify the amount of time to wait
	(in seconds) for the caller to answer before we consider our call attempt
	unsuccessful.

2.	:attr:`~pycall.Call.retry_time` lets you specify the amount of time to wait
	(in seconds) between retries. Let's say you try to call the number
	1-800-222-3333 but they don't answer, Asterisk will wait for
	:attr:`~pycall.Call.retry_time` seconds before calling the person again.

3.	:attr:`~pycall.Call.max_retries` lets you specify the maximum amount of
	retry attempts (you don't want to call someone forever, do you?).

Using these attributes is simple: ::

	c = Call('SIP/flowroute/18002223333', wait_time=10, retry_time=60,
			max_retries=2)


Archiving Call Files
--------------------

If, for some reason, you want to archive call files that have already been
spooled with Asterisk, just set the :attr:`~pycall.CallFile.archive` attribute
to `True`: ::

	cf = CallFile(..., archive=True)

and Asterisk will copy the call file (with a status code) to the archive
directory (typically `/var/spool/asterisk/outgoing_done`).


Dealing with Non-Standard Asterisk Installs
-------------------------------------------

If your Asterisk server isn't installed with the defaults, chances are you need
to make some changes. pycall provides a ton of flexibility in this regard, so
you should have no problems getting things running.

Specifying a Specific Name for Call Files
*****************************************

If you need to name your call file something special, just specify a value for
both the :attr:`~pycall.CallFile.filename` and :attr:`~pycall.CallFile.tempdir`
attributes: ::

	cf = CallFile(..., filename='test.call', tempdir='/tmp')

.. note::

	By default, pycall will randomly generate a call file name.

Specifing a Custom Spooling Directory
*************************************

If you're Asterisk install doesn't spool to the default
`/var/spool/asterisk/outgoing` directory, you can override it with the
:attr:`~pycall.CallFile.spool_dir` attribute: ::

	cf = CallFile(..., spool_dir='/tmp/outgoing')

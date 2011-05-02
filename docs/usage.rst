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

Foreword
========

Read this before you get started with pycall. This hopefully answers some
questions you may have about the intention of the project, what it aims at, and
whether you should or should not be using it.

What is pycall?
---------------

pycall is a simple python library which helps Asterisk developers create and
use call files in their software. pycall's easy to use API lets you automate
phone calls, and helps develop reliable telephony applications.

What is Asterisk?
-----------------

Asterisk is a popular open source PBX (phone system) which many businesses and
hobbyists use for placing and receiving phone calls. Asterisk is also used for
a wide variety of other purposes, all relating to telephony and communications.

If you've never used Asterisk, head over to `the Asterisk website
<http://www.asterisk.org/>`_ for more information.

What Are Call Files?
--------------------

Since pycall is a python library for "creating and using Asterisk call files",
you may be wondering what a call file *actually* is. Call files are text files
that can be read by the Asterisk spooler daemon, which contain directives that
tell Asterisk to automatically generate calls.

In a nutshell, Asterisk call files allow developers to automatically generate
calls and launch programs through Asterisk, without any sort of complex network
API. Call files are a simple way to build telephony functionality into your
applications without using the somewhat buggy (and poorly documented) Asterisk
Manager Interface (AMI).

To learn more about call files, head over to the `VoIP Info call files page
<http://www.voip-info.org/wiki/index.php?page_id=354>`_.

Why Should I Use pycall?
------------------------

There are lots of reasons why you should use pycall. I could just be vague and
leave it at that, but you want to *real* reasons right?

*	**Simple**

	pycall uses standard Asterisk call file syntax, and tries not to stray from
	popular conventions.

*	**Object Oriented**

	pycall provides an intuitive object wrapper for Asterisk call files. It
	helps organize call files logically in memory.

	For example: say you are making a wake up call program which lets multiple
	hotel guests schedule wake up calls at certain times. To store such a large
	amount of calls and associate them with times, it only makes sense to use
	objects.

*	**Environmentally Friendly**

	Although pycall can't fix the hole in the ozone layer, it can make it easy
	for you to place calls from any environment.

	*	Regardless of the user / group that Asterisk runs as on your server,
		pycall can set call file permissions appropriately.

	*	If you are running Asterisk in a customized environment (maybe your
		spooling directory is not the default), pycall allows you to easily
		override all directory dependent options.

*	**Secure**

	pycall securely allocates temporary file space by querying the target
	operating system, ensuring that all call files are able to be created, even
	in the most locked down production environments.

*	**Efficient**

	pycall creates call files when needed, and takes care of the clean up too.
	It leaves no temporary files hanging around your operating system.

*	**Thoughtless**

	pycall makes call file creation and usage thoughtless. Why spend valuable
	development time mucking around with boring text files and spooling?

*	**Thread Safe**

	pycall is thread safe. This is a handy feature as many times developers use
	multiple threads in their applications to both stress test PBX systems and
	make large amounts of calls quickly.

*	**Well Documented**

	pycall has great documentation (but you already know that by now, right?)
	and good support. This website contains lots of valuable information, and
	our mailing list is extremely active and helpful. And if those aren't
	enough for you, we also have an IRC chatroom which you can join to get live
	help.

Target Audience
---------------

Is pycall for you? If you are developing a telephony application with Asterisk,
and your application code runs on your Asterisk server (or on a server which
has direct access to your Asterisk server), then pycall is the API for you.

pycall is extremely simple to use, and makes generating calls a breeze. It is
highly configurable, but has sensible defaults, so it can be used in almost any
Asterisk environment.

If you suddenly discover that your application grows larger than originally
intended, head over to the :ref:`scaling` chapter to learn how to make pycall
scale for large usage.

Satisfied? Then head over to the :ref:`installation` chapter to get started.

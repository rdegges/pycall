.. _installation:

Installation
============

There are several ways to install pycall, and each of them is very easy. The
best way to install pycall (in production environments) is to use virtualenv,
so let's look at that first.

virtualenv
----------

Virtualenv is what you want to use during development and (especially) in
production if you have shell access. So first: what does virtualenv do? It
sets up a small 'virtual environment' which provides local copies of Python and
all of your application's dependencies. This ensures that your application is
always guaranteed to work, regardless of whether or not any system wide updates
are applied that may cause compatibility issues with your application or its
dependencies.

So let's get down to it:

If you are using any UNIX-based operating system, chances are one of the
following two commands will work for you::

	$ sudo easy_install virtualenv

or even better::

	$ sudo pip install virtualenv

If those commands don't work for you, and you still don't have virtualenv
installed, speak to your system administrator and have her install it for you.
(If you're on Ubuntu, try ``sudo apt-get install python-virtualenv``).

Now that you've got virtualenv running, just fire up a shell and create your
own environment. I usually create an `env` folder within my project directory::

	$ mkdir myproject
	$ cd myproject
	$ virtualenv env
	New python executable in env/bin/python
	Installing setuptools............done.

Now you only have to activate it, whenever you work with it. On and UNIX-based
operating system, do the following::

	$ . env/bin/activate

(Note the whitespace between the dot and the script name. This means execute
this file in context of the shell. If the dot does not work for whatever reason
in your shell, try substituting it with ``source``)

Either way, you should now be using your virtualenv (see how the prompt of your
shell has changed to show the virtualenv).

Now you can just enter the following command to get pycall activated in your
virtualenv::

	$ easy_install pycall

After pycall is installed, you are good to go.

System Wide Installation
------------------------

If you'd like to install pycall globally on your system (so that all users can
access it without doing anything special), simply run `easy_install` with root
rights::

	$ sudo easy_install pycall

If (for some reason or another) you are unable to get `easy_install` working,
you can install pycall from source. Simply download the latest release of
pycall from our `Github project page
<http://github.com/comradeb14ck/pycall/downloads>`_ and run the following::

	$ tar zxvf pycall-<version>.tar.gz
	$ cd pycall-<version>
	$ sudo python setup.py install

And you're ready to roll!

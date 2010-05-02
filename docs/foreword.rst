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

What are Call Files?
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

.. _developing:

Developing
==========

Contributing code to pycall is easy. The codebase is simple, clear, and tested.
All ideas / patches / etc. are welcome.

This section covers everything you need to know to contribute code, please give
it a full read before submitting patches to the project.

Project Goals
-------------

The main goal of the pycall library is to provide a *simple* python wrapper for
generating Asterisk call files. I'd like to keep the project and codebase small
and concise. It would be easy to add features to pycall that fall outside of
its humble goals--however, please resist that urge :)

Before submitting patches that add functionality, please consider whether or
not the patch contributes to the overall project goals, or takes away from
them.

Code Organization
-----------------

pycall is broken up into several python modules to keep the code organized. To
start reading code, check out the `callfile.py` module. This contains the main
:class:`~callfile.CallFile` class that most users interact with.

Each :class:`~callfile.CallFile` requires an :class:`~actions.Action` to be
specified. The idea is that a :class:`~callfile.CallFile` should represent the
physical call file, whereas an :class:`~actions.Action` should represent the
behavior of the call file (what actions should our call file perform if the
call is answered?).

Actions can be either applications (:class:`~actions.Application`) or contexts
(:class:`~actions.Context`). Both applicatoins and contexts correspond to their
`Asterisk equivalents
<http://www.voip-info.org/wiki/view/Asterisk+auto-dial+out>`_.

Each :class:`~callfile.CallFile` must also specify a :class:`~call.Call`
object. :class:`~call.Call` objects specify the actual call information-- what
number to call, what callerid to use, etc.

If there are errors, pycall will raise a custom :class:`~errors.PycallError`
exception. The errors are very descriptive, and always point to a solution.

Tests
-----

pycall is fully tested. The project currently makes use of a full unit test
suite to ensure that code works as advertised. In order to run the test suite
for yourself, you need to install the `python-nose
<http://code.google.com/p/python-nose/>`_ library, then run `python setup.py
nosetests`. If you'd like to see the coverage reports, you should also install
the `coverage.py <http://nedbatchelder.com/code/coverage/>`_ library.

All unit tests are broken up into python modules by topic. This is done to help
keep separate test easy to work with.

If you submit a patch, please ensure that it doesn't break any tests. If you
submit tests with your patch, it makes it much easier for me to review patches
and integrate them.

Code Style
----------

When submitting patches, please make sure that your code follows pycall's style
guidelines. The rules are pretty simple: just make your code fit in nicely with
the current code!

pycall uses tabs instead of spaces, and uses standard `PEP8
<http://www.python.org/dev/peps/pep-0008/>`_ formatting for everything else.

If in doubt, just look at pre-existing code.

Documentation
-------------

One of pycall's goals is to be well documented. Users should be able to quickly
see how to use the library, and integrate it into their project within a few
minutes.

If you'd like to contribute documentation to the project, it is certainly
welcome. All documentation is written using `Sphinx
<http://sphinx.pocoo.org/>`_ and compiles to HTML and PDF formats.

Development Tracker
-------------------

pycall is proudly hosted at `Github <https://github.com/rdegges/pycall>`_. If
you'd like to view the source code, contribute to the project, file bug reports
or feature requests, please do so there.

Submitting Code
---------------

The best way to submit code is to `fork pycall on Github
<https://github.com/rdegges/pycall>`_, make your changes, then submit a pull
request.

If you're unfamiliar with forking on Github, please read this `awesome article
<http://www.lornajane.net/posts/2010/Contributing-to-Projects-on-GitHub>`_.

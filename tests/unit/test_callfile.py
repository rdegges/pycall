"""Unit tests for `pycall.callfile`."""

from unittest import TestCase

from nose.tools import assert_false, eq_, ok_, raises

from pycall import Application, Call, CallFile


class TestCallFile(TestCase):
	"""Run tests on the `CallFile` class."""

	def setUp(self):
		"""Setup some default variables for test usage."""
		self.call = Call('local/18882223333@outgoing')
		self.action = Application('Playback', 'hello-world')
		self.spool_dir = '/'

	@raises(TypeError)
	def test_create_callfile(self):
		"""Ensure creating an empty `CallFile` object fails."""
		CallFile()

	def test_callfile_attrs(self):
		"""Ensure `CallFile` attributes stick."""
		c = CallFile(0, 1, 2, 3, 4, 5, 6, 7)
		eq_(c.call, 0)
		eq_(c.action, 1)
		eq_(c.set_var, 2)
		eq_(c.archive, 3)
		eq_(c.user, 4)
		eq_(c.tmpdir, 5)
		eq_(c.file_name, 6)
		eq_(c.spool_dir, 7)

	def test_is_valid_valid_call_and_valid_action(self):
		"""Ensure `is_valid` works with a well-formed `call` attribute."""
		c = CallFile(self.call, self.action, spool_dir=self.spool_dir)
		ok_(c.is_valid())

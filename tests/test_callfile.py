"""Unit tests for `pycall.callfile`."""

from unittest import TestCase

from path import path
from nose.tools import assert_false, eq_, ok_, raises

from pycall import Application, Call, CallFile, ValidationError


class TestCallFile(TestCase):
	"""Run tests on the `CallFile` class."""

	def setUp(self):
		"""Setup some default variables for test usage."""
		self.call = Call('channel')
		self.action = Application('application', 'data')
		self.spool_dir = '/'

	def test_attrs_stick(self):
		"""Ensure attributes stick."""
		c = CallFile('call', 'action', 'archive', 'user', 'spool_dir')
		eq_(c.call, 'call')
		eq_(c.action, 'action')
		eq_(c.archive, 'archive')
		eq_(c.user, 'user')
		eq_(c.spool_dir, 'spool_dir')

	def test_attrs_default_spool_dir(self):
		"""Ensure default `spool_dir` attribute works."""
		c = CallFile(self.call, self.action)
		eq_(c.spool_dir, CallFile.DEFAULT_SPOOL_DIR)

	def test_str(self):
		"""Ensure `__str__` works."""
		c = CallFile(self.call, self.action, spool_dir=self.spool_dir)
		ok_('archive' in c.__str__() and 'user' in c.__str__() and
				'spool_dir' in c.__str__())

	def test_is_valid_valid_call(self):
		"""Ensure `is_valid` works using a valid `call` attribute."""
		c = CallFile(self.call, self.action, spool_dir=self.spool_dir)
		ok_(c.is_valid())

	def test_is_valid_valid_action(self):
		"""Ensure `is_valid` works using a valid `action` attribute."""
		c = CallFile(self.call, self.action, spool_dir=self.spool_dir)
		ok_(c.is_valid())

	def test_is_valid_valid_spool_dir(self):
		"""Ensure `is_valid` works using a valid `spool_dir` attribute."""
		c = CallFile(self.call, self.action, spool_dir=self.spool_dir)
		ok_(c.is_valid())

	def test_is_valid_valid_call_is_valid(self):
		"""Ensure `is_valid` works when `call.is_valid()` works."""
		c = CallFile(self.call, self.action, spool_dir=self.spool_dir)
		ok_(c.is_valid())

	def test_is_valid_invalid_call(self):
		"""Ensure `is_valid` fails given an invalid `call` attribute."""
		c = CallFile('call', self.action, spool_dir=self.spool_dir)
		assert_false(c.is_valid())

	def test_is_valid_invalid_action(self):
		"""Ensure `is_valid` fails given an invalid `action` attribute."""
		c = CallFile(self.call, 'action', spool_dir=self.spool_dir)
		assert_false(c.is_valid())

	def test_is_valid_invalid_spool_dir(self):
		"""Ensure `is_valid` fails given an invalid `spool_dir` attribute."""
		c = CallFile(self.call, self.action, spool_dir='/woot')
		assert_false(c.is_valid())

	def test_is_valid_invalid_call_is_valid(self):
		"""Ensure `is_valid` fails when `call.is_valid()` fails."""
		c = CallFile(Call('channel', wait_time='10'), self.action,
				spool_dir=self.spool_dir)
		assert_false(c.is_valid())

	def test_buildfile_is_valid(self):
		"""Ensure `buildfile` works with well-formed attributes."""
		c = CallFile(self.call, self.action, spool_dir=self.spool_dir)
		ok_(c.buildfile())

	@raises(ValidationError)
	def test_buildfile_raises_validation_error(self):
		"""Ensure `buildfile` raises `ValidationError` if the `CallFile` can't
		be validated.
		"""
		CallFile(self.call, self.action, spool_dir='/woot').buildfile()

	def test_buildfile_valid_archive(self):
		"""Ensure that `buildfile` works with a well-formed `archive`
		attribute.
		"""
		c = CallFile(self.call, self.action, archive=True,
				spool_dir=self.spool_dir)
		ok_('Archive: yes' in ''.join(c.buildfile()))

	def test_buildfile_invalid_archive(self):
		"""Ensure `buildfile` works when `archive` is false."""
		c = CallFile(self.call, self.action, spool_dir=self.spool_dir)
		assert_false('Archive:' in ''.join(c.buildfile()))

	def test_contents(self):
		"""Ensure that the `contents` property works."""
		c = CallFile(self.call, self.action, spool_dir=self.spool_dir)
		ok_('channel' in c.contents and
				'application' in c.contents and 'data' in c.contents)

	def test_writefile_creates_file(self):
		"""Ensure that `writefile` actually generates a call file on the disk.
		"""
		c = CallFile(self.call, self.action, spool_dir=self.spool_dir)
		ok_(path(c.writefile()).abspath().exists())

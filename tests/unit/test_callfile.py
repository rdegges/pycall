"""Unit tests for `pycall.callfile`."""

from unittest import TestCase

from path import path
from nose.tools import assert_false, eq_, ok_, raises

from pycall import Application, Call, CallFile, ValidationError


class TestCallFile(TestCase):
	"""Run tests on the `CallFile` class."""

	def setUp(self):
		"""Setup some default variables for test usage."""
		self.call = Call('local/18882223333@outgoing')
		self.action = Application('Playback', 'hello-world')
		self.variables = {'a': 'b', 'c': 'd'}
		self.spool_dir = '/'

	def test_attrs_stick(self):
		"""Ensure attributes stick."""
		c = CallFile(0, 1, 2, 3, 4)
		eq_(c.call, 0)
		eq_(c.action, 1)
		eq_(c.archive, 2)
		eq_(c.user, 3)
		eq_(c.spool_dir, 4)

	def test_attrs_default_spool_dir(self):
		"""Ensure default `spool_dir` attribute works."""
		c = CallFile(self.call, self.action)
		eq_(c.spool_dir, CallFile.DEFAULT_SPOOL_DIR)

	def test_is_valid_valid_call(self):
		"""Ensure `is_valid` works using a valid `call` attribute."""
		c = CallFile(self.call, self.action, spool_dir=self.spool_dir)
		ok_(c.is_valid())

	def test_is_valid_valid_action(self):
		"""Ensure `is_valid` works using a valid `action` attribute."""
		c = CallFile(self.call, self.action, spool_dir=self.spool_dir)
		ok_(c.is_valid())

	def test_is_valid_valid_variables(self):
		"""Ensure `is_valid` works using a valid `variables` attribute."""
		c = CallFile(self.call, self.action, variables=self.variables,
				spool_dir=self.spool_dir)
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

	def test_is_valid_invalid_variables(self):
		"""Ensure `is_valid` fails given an invalid `variables` attribute."""
		c = CallFile(self.call, self.action, variables='variables',
				spool_dir=self.spool_dir)
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

	def test_buildfile_valid_variables(self):
		"""Ensure that `buildfile` works with a well-formed `variables`
		attribute.
		"""
		c = CallFile(self.call, self.action, variables={'hi': 'there'},
				spool_dir=self.spool_dir)
		ok_('hi=there' in ''.join(c.buildfile()))

	def test_buildfile_valid_archive(self):
		"""Ensure that `buildfile` works with a well-formed `archive`
		attribute.
		"""
		c = CallFile(self.call, self.action, archive=True,
				spool_dir=self.spool_dir)
		ok_('Archive: yes' in ''.join(c.buildfile()))

	def test_contents(self):
		"""Ensure that the `contents` property works."""
		c = CallFile(self.call, self.action, spool_dir=self.spool_dir)
		ok_('local/18882223333@outgoing' in c.contents and
				'Playback' in c.contents and 'hello-world' in c.contents)

	def test_writefile_creates_file(self):
		"""Ensure that `writefile` actually generates a call file on the disk.
		"""
		c = CallFile(self.call, self.action, spool_dir=self.spool_dir)
		ok_(path(c.writefile()).abspath().exists())

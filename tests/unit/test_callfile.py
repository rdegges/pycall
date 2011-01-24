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
		self.spool_dir = '/'

	@raises(TypeError)
	def test_create_callfile(self):
		"""Ensure creating an empty `CallFile` object fails."""
		CallFile()

	def test_callfile_attrs(self):
		"""Ensure `CallFile` attributes stick."""
		c = CallFile(0, 1, 2, 3, 4, 5, 6)
		eq_(c.call, 0)
		eq_(c.action, 1)
		eq_(c.variables, 2)
		eq_(c.archive, 3)
		eq_(c.user, 4)
		eq_(c._filename, 5)
		eq_(c.spool_dir, 6)

	def test_is_valid_valid_call_and_valid_action_and_valid_spool_dir(self):
		"""Ensure `is_valid` works with well-formed `call`, `action`, and
		`spool_dir` attributes."""
		c = CallFile(self.call, self.action, spool_dir=self.spool_dir)
		ok_(c.is_valid())

	def test_is_valid_invalid_call(self):
		"""Ensure `is_valid` fails with an invalid `call` attribute."""
		c = CallFile('call', self.action, spool_dir=self.spool_dir)
		assert_false(c.is_valid())

	def test_is_valid_invalid_call_validation(self):
		"""Ensure that the `call` attribute's `is_valid` method fails if the
		`Call` object is invalid.
		"""
		c = CallFile(Call('local/18882223333@outgoing', wait_time='wait_time'),
				self.action, spool_dir=self.spool_dir)
		assert_false(c.is_valid())

	def test_is_valid_invalid_action(self):
		"""Ensure `is_valid` fails with an invalid `action` attribute."""
		c = CallFile(self.call, 'action', spool_dir=self.spool_dir)
		assert_false(c.is_valid())

	def test_is_valid_valid_variables(self):
		"""Ensure `is_valid` works with a well-formed `variables` attribute."""
		c = CallFile(self.call, self.action, variables={'a': 'b'},
				spool_dir=self.spool_dir)
		ok_(c.is_valid())

	def test_is_valid_invalid_variables(self):
		"""Ensure `is_valid` fails with an invalid `variables` attribute."""
		c = CallFile(self.call, self.action, variables='variables',
				spool_dir=self.spool_dir)
		assert_false(c.is_valid())

	def test_is_valid_valid__filename(self):
		"""Ensure `is_valid` works with a well-formed `_filename` attribute."""
		c = CallFile(self.call, self.action, _filename='/test.call',
				spool_dir=self.spool_dir)
		ok_(c.is_valid())

	def test_is_valid_invalid__filename(self):
		"""Ensure `is_valid` fails with an invalid `_filename` attribute."""
		c = CallFile(self.call, self.action, _filename='/woot/lol/hi.txt',
				spool_dir=self.spool_dir)
		assert_false(c.is_valid())

	def test_is_valid_invalid_spool_dir(self):
		"""Ensure `is_valid` fails with an invalid `spool_dir` attribute."""
		c = CallFile(self.call, self.action, spool_dir='spool_dir')
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
		CallFile(self.call, self.action, tmpdir='tmpdir').buildfile()

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

	def test_filename(self):
		"""Ensure that the `filename` property works with a well-formed
		`_filename` attribute.
		"""
		c = CallFile(self.call, self.action, _filename='/woot.call',
				spool_dir=self.spool_dir)
		eq_(c.filename, 'woot.call')

	def test_writefile_creates_file(self):
		"""Ensure that `writefile` actually generates a call file on the disk.
		"""
		c = CallFile(self.call, self.action, spool_dir=self.spool_dir)
		ok_(path(c.writefile()).abspath().exists())

"""Unit tests for `pycall.actions`."""


from unittest import TestCase

from nose.tools import eq_, ok_

from pycall import Application, Context


class TestApplication(TestCase):
	"""Run tests on the `Application` class."""

	def setUp(self):
		"""Setup some default variables for test usage."""
		self.a = Application('application', 'data')

	def test_attrs_stick(self):
		"""Ensure attributes stick."""
		eq_(self.a.application, 'application')
		eq_(self.a.data, 'data')

	def test_render_valid_application(self):
		"""Ensure `render` works using a valid `application` attribute."""
		ok_('application' in ''.join(self.a.render()))

	def test_str_valid_data(self):
		"""Ensure `render` works using a valid `data` attribute."""
		ok_('data' in ''.join(self.a.render()))


class TestContext(TestCase):
	"""Run tests on the `Context` class."""

	def setUp(self):
		"""Setup some default variables for test usage."""
		self.c = Context('context', 'extension', 'priority')

	def test_attrs_stick(self):
		"""Ensure attributes stick."""
		eq_(self.c.context, 'context')
		eq_(self.c.extension, 'extension')
		eq_(self.c.priority, 'priority')

	def test_render_valid_context(self):
		"""Ensure `render` works using a valid `context` attribute."""
		ok_('context' in ''.join(self.c.render()))

	def test_render_valid_extension(self):
		"""Ensure `render` works using a valid `extension` attribute."""
		ok_('extension' in ''.join(self.c.render()))

	def test_render_valid_priority(self):
		"""Ensure `render` works using a valid `priority` attribute."""
		ok_('priority' in ''.join(self.c.render()))

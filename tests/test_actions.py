"""Unit tests for `pycall.actions`."""


from unittest import TestCase

from nose.tools import eq_, ok_, raises

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

	def test_str_valid_application(self):
		"""Ensure `__str__` works using test data."""
		ok_('application' in ''.join(self.a.__str__()) and
				'data' in ''.join(self.a.__str__()))


class TestContext(TestCase):
	"""Run tests on the `Context` class."""

	def setUp(self):
		"""Setup some default variables for test usage."""
		self.c = Context('context', 'extension', 'priority')

	def test_context_attrs(self):
		"""Ensure that all `Context` attributes stick."""
		c = Context('Callout', 's', '1')
		eq_(c.context, 'Callout')
		eq_(c.extension, 's')
		eq_(c.priority, '1')

	def test_context_str(self):
		"""Ensure the `__str__` method works."""
		c = Context('Callout', 's', '1')
		ok_('Callout' in ''.join(c.__str__()) and
				's' in ''.join(c.__str__()) and '1' in ''.join(c.__str__()))

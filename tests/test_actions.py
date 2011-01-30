"""Unit tests for `pycall.actions`."""


from unittest import TestCase

from nose.tools import eq_, ok_, raises

from pycall import Application, Context


class TestApplication(TestCase):
	"""Run tests on the `Application` class."""

	def test_attrs_stick(self):
		"""Ensure attributes stick."""
		a = Application('application', 'data')
		eq_(a.application, 'application')
		eq_(a.data, 'data')

	def test_application_str(self):
		"""Ensure the `__str__` method works."""
		a = Application('Playback', 'hello-world')
		ok_('Playback' in ''.join(a.__str__()) and
				'hello-world' in ''.join(a.__str__()))


class TestContext(TestCase):
	"""Test the `pycall.actions.Context` class."""

	@raises(TypeError)
	def test_create_context(self):
		"""Ensure creating an empty `Context` object fails."""
		Context()

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

"""Unit tests for `pycall.actions`."""


from unittest import TestCase

from nose.tools import eq_, raises

from pycall import Application, Context


class TestApplication(TestCase):
	"""Test the `pycall.actions.Application` class."""

	@raises(TypeError)
	def test_create_application(self):
		"""Ensure creating an empty `Application` object fails."""
		Application()

	def test_application_attrs(self):
		"""Ensure that all `Application` attributes stick."""
		a = Application('Playback', 'hello-world')
		eq_(a.application, 'Playback')
		eq_(a.data, 'hello-world')


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

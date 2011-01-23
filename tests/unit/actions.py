"""Unit tests for `pycall.actions`."""


from unittest import TestCase

from nose.tools import raises

from pycall.actions import Application, Context


class TestApplication(TestCase):
	"""Test the `pycall.actions.Application` class."""

	@raises(TypeError)
	def test_create_application(self):
		"""Ensure creating an empty `Application` object fails."""
		Application()


class TestContext(TestCase):
	"""Test the `pycall.actions.Context` class."""

	@raises(TypeError)
	def test_create_context(self):
		"""Ensure creating an empty `Context` object fails."""
		Context()

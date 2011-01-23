"""Unit tests for `pycall`."""

from unittest import TestCase

from nose.tools import raises

from pycall import CallFile


class TestCallFile(TestCase):
	"""Run tests on the `CallFile` class."""

	@raises(TypeError)
	def test_create_callfile(self):
		"""Ensure creating an empty `CallFile` object fails."""
		CallFile()

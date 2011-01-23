"""Unit tests for `pycall.call`."""


from unittest import TestCase

from nose.tools import eq_, raises

from pycall import Call


class TestCall(TestCase):
	"""Test the `pycall.call.Call` class."""

	@raises(TypeError)
	def test_create_call(self):
		"""Ensure creating an empty `Call` object fails."""
		Call()

	def test_call_attrs(self):
		"""Ensure that all `Call` attributes stick."""
		c = Call('local/18882223333@outgoing', '"Randall Degges" <666>',
				'rdegges', 10, 20)
		eq_(c.channel, 'local/18882223333@outgoing')
		eq_(c.callerid, '"Randall Degges" <666>')
		eq_(c.account, 'rdegges')
		eq_(c.wait_time, 10)
		eq_(c.max_retries, 20)

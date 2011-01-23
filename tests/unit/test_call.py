"""Unit tests for `pycall.call`."""


from unittest import TestCase

from nose.tools import assert_false, eq_, ok_, raises

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
				'rdegges', 10, 15, 20)
		eq_(c.channel, 'local/18882223333@outgoing')
		eq_(c.callerid, '"Randall Degges" <666>')
		eq_(c.account, 'rdegges')
		eq_(c.wait_time, 10)
		eq_(c.retry_time, 15)
		eq_(c.max_retries, 20)

	def test_is_valid_no_wait_time_and_no_max_retries(self):
		"""Make sure we can pass `is_valid` checks with no `wait_time` or
		`max_retries` attributes specified.
		"""
		c = Call('local/18882223333@outgoing')
		ok_(c.is_valid())

	def test_is_valid_proper_wait_time(self):
		"""Ensure a valid `wait_time` attribute passes the `is_valid` check."""
		c = Call('local/18882223333@outgoing', wait_time=15)
		ok_(c.is_valid())

	def test_is_valid_proper_max_retries(self):
		"""Ensure a valid `max_retries` attribute passes the `is_valid` check.
		"""
		c = Call('local/18882223333@outgoing', max_retries=10)
		ok_(c.is_valid())

	def test_is_valid_bad_wait_time(self):
		"""Ensure a non-int `wait_time` attribute fails the `is_valid` check.
		"""
		c = Call('local/18882223333@outgoing', wait_time='15')
		assert_false(c.is_valid())

	def test_is_valid_bad_max_retries(self):
		"""Ensure a non-int `max_retries` attribute fails the `is_valid` check.
		"""
		c = Call('local/18882223333@outgoing', max_retries='10')
		assert_false(c.is_valid())

"""Unit tests for `pycall.call`."""


from unittest import TestCase

from nose.tools import assert_false, eq_, ok_

from pycall import Call


class TestCall(TestCase):
	"""Tests the `Call` class."""

	def test_attrs_stick(self):
		"""Ensure attributes stick."""
		c = Call('channel', 'callerid', 'account', 0, 1, 2)
		eq_(c.channel, 'channel')
		eq_(c.callerid, 'callerid')
		eq_(c.account, 'account')
		eq_(c.wait_time, 0)
		eq_(c.retry_time, 1)
		eq_(c.max_retries, 2)

	def test_is_valid_no_wait_time_and_no_retry_time_and_no_max_retries(self):
		"""Make sure we can pass `is_valid` checks with no `wait_time` or
		`retry_time` or `max_retries` attributes specified.
		"""
		c = Call('local/18882223333@outgoing')
		ok_(c.is_valid())

	def test_is_valid_proper_wait_time(self):
		"""Ensure a valid `wait_time` attribute passes the `is_valid` check."""
		c = Call('local/18882223333@outgoing', wait_time=15)
		ok_(c.is_valid())

	def test_is_valid_proper_retry_time(self):
		"""Ensure a valid `retry_time` attribute passes the `is_valid` check.
		"""
		c = Call('local/18882223333@outgoing', retry_time=17)
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

	def test_is_valid_bad_retry_time(self):
		"""Ensure a non-int `retry_time` attribute fails the `is_valid` check.
		"""
		c = Call('local/18882223333@outgoing', retry_time='17')
		assert_false(c.is_valid())

	def test_is_valid_bad_max_retries(self):
		"""Ensure a non-int `max_retries` attribute fails the `is_valid` check.
		"""
		c = Call('local/18882223333@outgoing', max_retries='10')
		assert_false(c.is_valid())

	def test_str_no_attrs(self):
		"""Ensure `__str__` works with no optional attributes specified."""
		c = Call('local/18882223333@outgoing')
		ok_('Channel: local/18882223333@outgoing' in ''.join(c.__str__()))

	def test_str_valid_callerid(self):
		"""Ensure `__str__` works with a well-formed `callerid` attribute."""
		c = Call('local/18882223333@outgoing', callerid='"hi"')
		ok_('"hi"' in ''.join(c.__str__()))

	def test_str_valid_account(self):
		"""Ensure `__str__` works with a well-formed `account` attribute."""
		c = Call('local/18882223333@outgoing', account='rdegges')
		ok_('rdegges' in ''.join(c.__str__()))

	def test_str_valid_wait_time(self):
		"""Ensure `__str__` works with a well-formed `wait_time` attribute."""
		c = Call('local/18882223333@outgoing', wait_time=10)
		ok_('10' in ''.join(c.__str__()))

	def test_str_valid_retry_time(self):
		"""Ensure `__str__` works with a well-formed `retry_time` attribute."""
		c = Call('local/18882223333@outgoing', retry_time=15)
		ok_('15' in ''.join(c.__str__()))

	def test_str_valid_max_retries(self):
		"""Ensure `__str__` works with a well-formed `max_retries`
		attribute.
		"""
		c = Call('local/18882223333@outgoing', max_retries=20)
		ok_('20' in ''.join(c.__str__()))

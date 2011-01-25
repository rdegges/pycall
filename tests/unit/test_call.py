"""Unit tests for `pycall.call`."""


from unittest import TestCase

from nose.tools import assert_false, eq_, ok_

from pycall import Call


class TestCall(TestCase):
	"""Run tests on the `Call` class."""

	def test_attrs_stick(self):
		"""Ensure attributes stick."""
		c = Call('channel', 'callerid', 'account', 0, 1, 2)
		eq_(c.channel, 'channel')
		eq_(c.callerid, 'callerid')
		eq_(c.account, 'account')
		eq_(c.wait_time, 0)
		eq_(c.retry_time, 1)
		eq_(c.max_retries, 2)

	def test_is_valid_valid_variables(self):
		"""Ensure `is_valid` works using a valid `variables` attribute."""
		c = Call('channel', variables={'a': 'b'})
		ok_(c.is_valid())

	def test_is_valid_valid_wait_time(self):
		"""Ensure `is_valid` works using a valid `wait_time` attribute."""
		c = Call('channel', wait_time=0)
		ok_(c.is_valid())

	def test_is_valid_valid_retry_time(self):
		"""Ensure `is_valid` works using a valid `retry_time` attribute."""
		c = Call('channel', retry_time=1)
		ok_(c.is_valid())

	def test_is_valid_valid_max_retries(self):
		"""Ensure `is_valid` works using a valid `max_retries` attribute."""
		c = Call('channel', max_retries=2)
		ok_(c.is_valid())

	def test_is_valid_invalid_variables(self):
		"""Ensure `is_valid` fails given an invalid `variables` attribute."""
		c = Call('channel', variables='ab')
		assert_false(c.is_valid())

	def test_is_valid_invalid_wait_time(self):
		"""Ensure `is_valid` fails given an invalid `wait_time` attribute."""
		c = Call('channel', wait_time='0')
		assert_false(c.is_valid())

	def test_is_valid_invalid_retry_time(self):
		"""Ensure `is_valid` fails given an invalid `retry_time` attribute."""
		c = Call('channel', retry_time='1')
		assert_false(c.is_valid())

	def test_is_valid_invalid_max_retries(self):
		"""Ensure `is_valid` fails given an invalid `max_retries` attribute."""
		c = Call('channel', max_retries='2')
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

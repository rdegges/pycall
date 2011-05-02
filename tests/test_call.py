"""Unit tests for `pycall.call`."""


from unittest import TestCase

from nose.tools import assert_false, eq_, ok_

from pycall import Call


class TestCall(TestCase):
	"""Run tests on the `Call` class."""

	def test_attrs_stick(self):
		"""Ensure attributes stick."""
		c = Call('channel', 'callerid', 'variables', 'account', 0, 1, 2)
		eq_(c.channel, 'channel')
		eq_(c.callerid, 'callerid')
		eq_(c.variables, 'variables')
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

	def test_render_valid_channel(self):
		"""Ensure `render` works using a valid `channel` attribute."""
		c = Call('channel')
		ok_('channel' in ''.join(c.render()))

	def test_render_valid_callerid(self):
		"""Ensure `render` works using a valid `callerid` attribute."""
		c = Call('channel', callerid='callerid')
		ok_('callerid' in ''.join(c.render()))

	def test_render_valid_variables(self):
		"""Ensure `render` works using a valid `variables` attribute."""
		c = Call('channel', variables={'a': 'b'})
		ok_('a=b' in ''.join(c.render()))

	def test_render_valid_account(self):
		"""Ensure `render` works using a valid `account` attribute."""
		c = Call('channel', account='account')
		ok_('account' in ''.join(c.render()))

	def test_render_valid_wait_time(self):
		"""Ensure `render` works using a valid `wait_time` attribute."""
		c = Call('channel', wait_time=0)
		ok_('0' in ''.join(c.render()))

	def test_render_valid_retry_time(self):
		"""Ensure `render` works using a valid `retry_time` attribute."""
		c = Call('channel', retry_time=1)
		ok_('1' in ''.join(c.render()))

	def test_render_valid_max_retries(self):
		"""Ensure `render` works using a valid `max_retries` attribute."""
		c = Call('channel', max_retries=2)
		ok_('2' in ''.join(c.render()))

	def test_render_no_attrs(self):
		"""Ensure `render` works with no optional attributes specified."""
		c = Call('local/18882223333@outgoing')
		ok_('Channel: local/18882223333@outgoing' in ''.join(c.render()))

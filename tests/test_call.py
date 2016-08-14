"""Unit tests for `pycall.call`."""


from unittest import TestCase

from pycall import Call


class TestCall(TestCase):
    """Run tests on the `Call` class."""

    def test_attrs_stick(self):
        """Ensure attributes stick."""
        c = Call('channel', 'callerid', 'variables', 'account', 0, 1, 2)
        self.assertEqual(c.channel, 'channel')
        self.assertEqual(c.callerid, 'callerid')
        self.assertEqual(c.variables, 'variables')
        self.assertEqual(c.account, 'account')
        self.assertEqual(c.wait_time, 0)
        self.assertEqual(c.retry_time, 1)
        self.assertEqual(c.max_retries, 2)

    def test_is_valid_valid_variables(self):
        """Ensure `is_valid` works using a valid `variables` attribute."""
        c = Call('channel', variables={'a': 'b'})
        self.assertTrue(c.is_valid())

    def test_is_valid_valid_wait_time(self):
        """Ensure `is_valid` works using a valid `wait_time` attribute."""
        c = Call('channel', wait_time=0)
        self.assertTrue(c.is_valid())

    def test_is_valid_valid_retry_time(self):
        """Ensure `is_valid` works using a valid `retry_time` attribute."""
        c = Call('channel', retry_time=1)
        self.assertTrue(c.is_valid())

    def test_is_valid_valid_max_retries(self):
        """Ensure `is_valid` works using a valid `max_retries` attribute."""
        c = Call('channel', max_retries=2)
        self.assertTrue(c.is_valid())

    def test_is_valid_invalid_variables(self):
        """Ensure `is_valid` fails given an invalid `variables` attribute."""
        c = Call('channel', variables='ab')
        self.assertFalse(c.is_valid())

    def test_is_valid_invalid_wait_time(self):
        """Ensure `is_valid` fails given an invalid `wait_time` attribute."""
        c = Call('channel', wait_time='0')
        self.assertFalse(c.is_valid())

    def test_is_valid_invalid_retry_time(self):
        """Ensure `is_valid` fails given an invalid `retry_time` attribute."""
        c = Call('channel', retry_time='1')
        self.assertFalse(c.is_valid())

    def test_is_valid_invalid_max_retries(self):
        """Ensure `is_valid` fails given an invalid `max_retries` attribute."""
        c = Call('channel', max_retries='2')
        self.assertFalse(c.is_valid())

    def test_render_valid_channel(self):
        """Ensure `render` works using a valid `channel` attribute."""
        c = Call('channel')
        self.assertTrue('channel' in ''.join(c.render()))

    def test_render_valid_callerid(self):
        """Ensure `render` works using a valid `callerid` attribute."""
        c = Call('channel', callerid='callerid')
        self.assertTrue('callerid' in ''.join(c.render()))

    def test_render_valid_variables(self):
        """Ensure `render` works using a valid `variables` attribute."""
        c = Call('channel', variables={'a': 'b'})
        self.assertTrue('a=b' in ''.join(c.render()))

    def test_render_valid_account(self):
        """Ensure `render` works using a valid `account` attribute."""
        c = Call('channel', account='account')
        self.assertTrue('account' in ''.join(c.render()))

    def test_render_valid_wait_time(self):
        """Ensure `render` works using a valid `wait_time` attribute."""
        c = Call('channel', wait_time=0)
        self.assertTrue('0' in ''.join(c.render()))

    def test_render_valid_retry_time(self):
        """Ensure `render` works using a valid `retry_time` attribute."""
        c = Call('channel', retry_time=1)
        self.assertTrue('1' in ''.join(c.render()))

    def test_render_valid_max_retries(self):
        """Ensure `render` works using a valid `max_retries` attribute."""
        c = Call('channel', max_retries=2)
        self.assertTrue('2' in ''.join(c.render()))

    def test_render_no_attrs(self):
        """Ensure `render` works with no optional attributes specified."""
        c = Call('local/18882223333@outgoing')
        self.assertTrue('Channel: local/18882223333@outgoing' in ''.join(c.render()))

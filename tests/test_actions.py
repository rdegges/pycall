"""Unit tests for `pycall.actions`."""


from unittest import TestCase

from pycall import Application, Context


class TestApplication(TestCase):
    """Run tests on the `Application` class."""

    def setUp(self):
        """Setup some default variables for test usage."""
        self.a = Application('application', 'data')

    def test_attrs_stick(self):
        """Ensure attributes stick."""
        self.assertEqual(self.a.application, 'application')
        self.assertEqual(self.a.data, 'data')

    def test_render_valid_application(self):
        """Ensure `render` works using a valid `application` attribute."""
        self.assertTrue('application' in ''.join(self.a.render()))

    def test_str_valid_data(self):
        """Ensure `render` works using a valid `data` attribute."""
        self.assertTrue('data' in ''.join(self.a.render()))


class TestContext(TestCase):
    """Run tests on the `Context` class."""

    def setUp(self):
        """Setup some default variables for test usage."""
        self.c = Context('context', 'extension', 'priority')

    def test_attrs_stick(self):
        """Ensure attributes stick."""
        self.assertEqual(self.c.context, 'context')
        self.assertEqual(self.c.extension, 'extension')
        self.assertEqual(self.c.priority, 'priority')

    def test_render_valid_context(self):
        """Ensure `render` works using a valid `context` attribute."""
        self.assertTrue('context' in ''.join(self.c.render()))

    def test_render_valid_extension(self):
        """Ensure `render` works using a valid `extension` attribute."""
        self.assertTrue('extension' in ''.join(self.c.render()))

    def test_render_valid_priority(self):
        """Ensure `render` works using a valid `priority` attribute."""
        self.assertTrue('priority' in ''.join(self.c.render()))

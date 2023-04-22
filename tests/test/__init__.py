"""Root class for testing telegram.email.notify."""
from tester_flask import TestFlask
from test_helper_gae3 import TestGae3


class TestCase(TestFlask, TestGae3):
    """Base class."""

    def setUp(self, app):  # pylint: disable=arguments-differ
        """Set up tests."""
        TestFlask.setUp(self, app)
        TestGae3.set_up(self)

    def tearDown(self):
        """Clear tests."""
        TestGae3.tear_down(self)
        super().tearDown()

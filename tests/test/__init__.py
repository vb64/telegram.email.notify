"""
Root class for testing telegram.email.notify
"""
from tester_flask import TestFlask


class TestCase(TestFlask):
    """
    Base class
    """
    def setUp(self):  # pylint: disable=arguments-differ
        from wsgi import app
        TestFlask.setUp(self, app)

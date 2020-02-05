"""
Root class for testing telegram.email.notify
"""
import os
from tester_flask import TestFlask


class TestCase(TestFlask):
    """
    Base class
    """
    def setUp(self):  # pylint: disable=arguments-differ
        from wsgi import app
        TestFlask.setUp(self, app)

    @staticmethod
    def get_fixture(file_name):
        """
        load content of given file
        """
        return open(os.path.join("tests", "fixture", file_name)).read()

"""
Root class for testing telegram.email.notify
"""
import os
from tester_flask import TestFlask
from tester_gae import TestGae


class TestCase(TestFlask, TestGae):
    """
    Base class
    """
    def setUp(self):  # pylint: disable=arguments-differ
        from wsgi import app
        from appengine_config import PROJECT_DIR

        TestFlask.setUp(self, app)
        TestGae.setUp(self, PROJECT_DIR)

    def tearDown(self):
        TestGae.tearDown(self)

    @staticmethod
    def get_fixture(file_name):
        """
        load content of given file
        """
        return open(os.path.join("tests", "fixture", file_name)).read()

    def start_transfer(self, fname, start_func, label):
        """
        run start function
        """
        lines = self.get_fixture(os.path.join(label, fname)).splitlines()
        subj = lines[0]
        text = '\n'.join(lines[1:])

        return start_func(subj, text)

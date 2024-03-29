"""Root class for testing telegram.email.notify."""
import os
from .. import TestCase


class TestDefault(TestCase):
    """Base class for default service."""

    def setUp(self):  # pylint: disable=arguments-differ
        """Set up tests."""
        from main import app
        TestCase.setUp(self, app)

    @staticmethod
    def get_fixture_path(file_name):
        """Fixture path for given file."""
        return os.path.join("tests", "fixture", file_name)

    def get_fixture(self, file_name):
        """Load content of given file."""
        return open(self.get_fixture_path(file_name), encoding='utf-8').read()

    def start_transfer(self, fname, start_func, label):
        """Run start function."""
        lines = self.get_fixture(os.path.join(label, fname)).splitlines()
        subj = lines[0]
        text = '\n'.join(lines[1:])

        return start_func(subj, text)

    def start_eml(self, fname, start_func, label):
        """Run start function with data from eml file."""
        from models import EmailData

        fname = self.get_fixture_path(os.path.join(label, fname))
        edata = EmailData.from_upload(open(fname, encoding='utf-8'))
        text = edata.field_text + '\n' + edata.field_html

        return start_func(edata.field_subj, text)

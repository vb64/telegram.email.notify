"""Google Alerts.

make test T=test_default/test_modules/test_galerts.py
"""
from . import TestModule


class TestGalerts(TestModule):
    """Google Alerts."""

    def transfer(self, fname):
        """Transfer fixture by Google Alerts."""
        from modules.galerts import start
        return self.start_transfer(fname, start, 'galerts')

    def from_eml(self, fname):
        """Fixture from eml file Google Alerts."""
        from modules.galerts import start
        return self.start_eml(fname, start, 'galerts')

    def test_dflt(self):
        """Default."""
        from modutil import MARKUP

        text = self.transfer('alert1.txt')
        assert MARKUP in text

    @staticmethod
    def test_alert_ru():
        """Check alert_ru."""
        from modules.galerts import alert_ru
        assert len(alert_ru('subj', 'body')) == 4

    @staticmethod
    def test_start():
        """Start."""
        from modules.galerts import start

        assert start('subj', 'body') == 'subj\nbody'

    def test_02(self):
        """Check alert2.txt."""
        from modutil import MARKUP

        text = self.transfer('alert2.txt')
        assert MARKUP in text

    def test_03(self):
        """Check alert3.txt."""
        from modutil import MARKUP

        text = self.transfer('alert3.txt')
        assert MARKUP in text

    def test_eml(self):
        """Check galerts01.eml."""
        from modutil import MARKUP

        text = self.from_eml('galerts01.eml')
        assert MARKUP in text

        text = self.from_eml('galerts02.eml')
        assert MARKUP in text

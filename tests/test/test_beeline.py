"""
make test T=test_beeline.py
"""
from . import TestCase


class TestBeeline(TestCase):
    """
    Beeline
    """
    def transfer(self, fname):
        """
        transfer fixture by beeline
        """
        from modules.beeline import start
        return self.start_transfer(fname, start, 'beeline')

    def test_voice_mail(self):
        """
        voice mail
        """
        text = self.transfer('voice_mail.txt')

        assert text

"""
make test T=test_youtube.py
"""
from . import TestCase


class TestYouTube(TestCase):
    """
    YouTube
    """
    def transfer(self, fname):
        """
        transfer fixture by YouTube
        """
        from modules.youtube import start
        return self.start_transfer(fname, start, 'youtube')

    def test_msg(self):
        """
        notify
        """
        mark = "https://www.youtube.com/account_notifications?feature"

        text = self.transfer('vspishka.txt')
        assert mark not in text

        text = self.transfer('ezhik.txt')
        assert mark not in text

    def test_nolink(self):
        """
        no link notify
        """
        mark = "https://www.youtube.com/account_notifications?feature"
        text = self.transfer('nolink.txt')
        assert mark not in text

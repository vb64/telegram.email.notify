"""Youtube.

make test T=test_modules/test_youtube.py
"""
from . import TestModule


class TestYouTube(TestModule):
    """YouTube."""

    def transfer(self, fname):
        """Transfer fixture by YouTube."""
        from modules.youtube import start
        return self.start_transfer(fname, start, 'youtube')

    def test_msg(self):
        """Notify."""
        mark = "https://www.youtube.com/account_notifications?feature"

        text = self.transfer('vspishka.txt')
        assert mark not in text

        text = self.transfer('ezhik.txt')
        assert mark not in text

        text = self.transfer('upload.txt')
        assert mark not in text

        text = self.transfer('upload1.txt')
        assert mark not in text

    def test_nolink(self):
        """No link notify."""
        mark = "https://www.youtube.com/account_notifications?feature"
        text = self.transfer('nolink.txt')
        assert mark not in text

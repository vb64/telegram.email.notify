"""
make test T=test_youtube.py
"""
import os
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

        lines = self.get_fixture(os.path.join('youtube', fname)).splitlines()
        subj = lines[0]
        text = '\n'.join(lines[1:])

        return start(subj, text)

    def test_yt_msg(self):
        """
        wrong youtube notify
        """
        mark = "https://money.yandex.ru/i/html"
        text = self.transfer('pay.txt')

        assert mark not in text

"""
make test T=test_fb.py
"""
import os
from . import TestCase


class TestFB(TestCase):
    """
    FaceBook
    """
    def transfer(self, fname):
        """
        transfer fixture by facebook
        """
        from modules.fb import start

        lines = self.get_fixture(os.path.join('fb', fname)).splitlines()
        subj = lines[0]
        text = '\n'.join(lines[1:])

        return start(subj, text)

    def test_msg(self):
        """
        ym notify (wrong)
        """
        mark = "https://money.yandex.ru/i/html-letters"
        text = self.transfer('pay.txt')

        assert mark not in text

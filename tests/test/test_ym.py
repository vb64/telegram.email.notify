"""
make test T=test_ym.py
"""
import os
from . import TestCase


class TestYM(TestCase):
    """
    Yandex Money
    """
    def test_pay(self):
        """
        pay notify
        """
        from modules.ym import start

        mark = "(https://money.yandex.ru/i/html-letters/header__logo.png)"
        text = start(self.get_fixture(os.path.join('ym', 'pay.txt')))

        assert mark not in text
        # print unicode(text, 'utf8')

"""
make test T=test_ym.py
"""
import os
from . import TestCase


class TestYM(TestCase):
    """
    Yandex Money
    """
    def transfer(self, fname):
        """
        transfer fixture by ym
        """
        from modules.ym import start

        return start(self.get_fixture(os.path.join('ym', fname)))

    def test_pay(self):
        """
        pay notify
        """
        mark = "(https://money.yandex.ru/i/html-letters/header__logo.png)"
        text = self.transfer('pay.txt')

        assert mark not in text

    def test_other(self):
        """
        other notify
        """
        assert self.transfer('cash.txt')
        assert self.transfer('cashback.txt')
        assert self.transfer('income.txt')
        assert self.transfer('transfer_in.txt')
        assert self.transfer('weekly.txt')
        assert self.transfer('transfer_out.txt')

        # print '\n##', self.transfer('transfer_out.txt')
        # print '\n##', self.transfer('cash.txt')
        # print '\n##', self.transfer('cashback.txt')
        # print '\n##', self.transfer('income.txt')
        # print '\n##', self.transfer('transfer_in.txt')
        # print '\n##', self.transfer('weekly.txt')

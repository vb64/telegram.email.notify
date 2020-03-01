"""
make test T=test_ym.py
"""
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
        return self.start_transfer(fname, start, 'ym')

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
        assert self.transfer('pay_card.txt')
        assert self.transfer('pay_wallet.txt')
        assert self.transfer('transfer_in1.txt')
        assert self.transfer('pay_wallet1.txt')

        assert self.transfer('transfer_in2.txt')
        print '\n##', self.transfer('transfer_in2.txt')

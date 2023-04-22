"""Yandex Money.

make test T=test_modules/test_ym.py
"""
from . import TestModule


class TestYM(TestModule):
    """Yandex Money."""

    def transfer(self, fname):
        """Transfer fixture by ym."""
        from modules.ym import start
        return self.start_transfer(fname, start, 'ym')

    def test_pay(self):
        """Pay notify."""
        mark = "(https://money.yandex.ru/i/html-letters/header__logo.png)"
        text = self.transfer('pay.txt')

        assert mark not in text

    def test_other(self):
        """Other notify."""
        assert self.transfer('cash.txt')
        assert self.transfer('cashback.txt')
        assert self.transfer('income.txt')
        assert self.transfer('transfer_in.txt')
        assert self.transfer('transfer_out.txt')
        assert self.transfer('pay_card.txt')
        assert self.transfer('pay_wallet.txt')
        assert self.transfer('transfer_in1.txt')
        assert self.transfer('pay_wallet1.txt')
        assert self.transfer('transfer_in2.txt')

    def test_subjonly(self):
        """Subj only."""
        assert "Вход куда-то от имени клиента" in self.transfer('subjonly.txt')

    def test_week(self):
        """Check week1."""
        text = self.transfer('weekly1.txt')
        assert "баланс на 1 августа" in text

# -*- coding: utf-8 -*-
"""
make test T=test_galerts.py
"""
from . import TestCase


class TestGalerts(TestCase):
    """
    Google Alerts
    """
    def transfer(self, fname):
        """
        transfer fixture by Google Alerts
        """
        from modules.galerts import start
        return self.start_transfer(fname, start, 'galerts')

    def test_dflt(self):
        """
        default
        """
        from modules import MARKUP

        text = self.transfer('alert1.txt')
        assert MARKUP in text
        # print text.encode('cp866', 'ignore')

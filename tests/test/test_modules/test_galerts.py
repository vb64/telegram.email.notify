# -*- coding: utf-8 -*-
"""
make test T=test_modules/test_galerts.py
"""
from . import TestModule


class TestGalerts(TestModule):
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

    @staticmethod
    def test_alert_ru():
        """
        alert_ru
        """
        from modules.galerts import alert_ru
        assert len(alert_ru('subj', 'body')) == 4

    @staticmethod
    def test_start():
        """
        start
        """
        from modules.galerts import start

        assert start('subj', 'body') == 'subj\nbody'

    def test_02(self):
        """
        alert2.txt
        """
        from modules import MARKUP

        text = self.transfer('alert2.txt')
        assert MARKUP in text

    def test_03(self):
        """
        alert3.txt
        """
        from modules import MARKUP

        text = self.transfer('alert3.txt')
        assert MARKUP in text
        # print text.decode('utf-8').encode('cp866', 'ignore')

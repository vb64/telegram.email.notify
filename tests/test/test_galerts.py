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

    @staticmethod
    def test_add_href():
        """
        add_href
        """
        from modules.galerts import add_href

        words = []
        add_href(words, 'xxx')
        assert words == [('xxx', False)]

        words = [('xxx', True)]
        add_href(words, 'yyy')
        assert words == [('xxx', True), ('yyy', False)]

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
        # print text.encode('cp866', 'ignore')

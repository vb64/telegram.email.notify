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

    def test_voice_mail(self):
        """
        voice mail
        """
        text = self.transfer('alert1.txt')
        print "###"
        print unicode(text, 'utf-8').encode('cp866', 'ignore')
        # assert 'XXXX' in text

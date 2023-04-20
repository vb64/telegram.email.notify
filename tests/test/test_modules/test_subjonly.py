"""Subject only module.

make test T=test_modules/test_subjonly.py
"""
from . import TestModule


class TestSubjonly(TestModule):
    """Subject only."""

    def transfer(self, fname):
        """Transfer fixture by beeline."""
        from modules.subjonly import start
        return self.start_transfer(fname, start, 'beeline')

    def test_voice_mail(self):
        """Voice mail messge."""
        text = self.transfer('voice_mail.txt')
        assert u'Облачная АТС - У вас новое сообщение голосовой почты' in text
        assert ' 9033756597' not in text

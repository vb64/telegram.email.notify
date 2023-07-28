"""Subject only module.

make test T=test_default/test_modules/test_subjonly.py
"""
from . import TestModule


class TestSubjonly(TestModule):
    """Subject only."""

    def from_eml(self, fname):
        """Fixture from eml file subjonly."""
        from modules.subjonly import start
        return self.start_eml(fname, start, 'subjonly')

    def transfer(self, fname):
        """Transfer fixture by beeline."""
        from modules.subjonly import start
        return self.start_transfer(fname, start, 'beeline')

    def test_voice_mail(self):
        """Voice mail messge."""
        text = self.transfer('voice_mail.txt')
        assert 'Облачная АТС - У вас новое сообщение голосовой почты' in text
        assert ' 9033756597' not in text

    def test_eml(self):
        """Check eml file."""
        text = self.from_eml('msg01.eml')
        assert 'Только тема' in text
        assert 'тело письма' not in text

"""Beeline.

make test T=test_modules/test_beeline.py
"""
from . import TestModule


class TestBeeline(TestModule):
    """Beeline."""

    def transfer(self, fname):
        """Transfer fixture by beeline."""
        from modules.beeline import start
        return self.start_transfer(fname, start, 'beeline')

    def test_voice_mail(self):
        """Voice mail."""
        text = self.transfer('voice_mail.txt')
        assert ' 9033756597' in text

    @staticmethod
    def test_voice_mail_func():
        """Voice mail function."""
        from modules.beeline import voice_mail

        text = ''.join((
          "В Ваш почтовый ящик поступило сообщекние. ",
          "Прослушать сообщение можно в web-интерфейсе управления услугой.",
        ))
        result = voice_mail('', text)
        assert 'cloudpbx.beeline.ru' in result[1]

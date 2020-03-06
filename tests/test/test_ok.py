"""
make test T=test_ok.py
"""
from . import TestCase


class TestOk(TestCase):
    """
    Odnoklassniki.ru
    """
    mark = "<html>"

    def transfer(self, fname):
        """
        transfer fixture by ok
        """
        from modules.ok import start
        return self.start_transfer(fname, start, 'ok')

    def test_message(self):
        """
        message
        """
        text = self.transfer('no_photo.txt')
        assert self.mark not in text

        text = self.transfer('message.txt')
        assert self.mark not in text

    def test_m(self):
        """
        mN
        """
        text = self.transfer('m1.txt')
        assert self.mark not in text

    def test_m2(self):
        """
        m2
        """
        text = self.transfer('m2.txt')
        assert self.mark not in text

    def test_present(self):
        """
        present
        """
        text = self.transfer('present1.txt')
        assert self.mark not in text

        text = self.transfer('present.txt')
        assert self.mark not in text
        # print "###"
        # print text

"""
make test T=test_lj.py
"""
from . import TestCase


class TestLj(TestCase):
    """
    LiveJournal
    """
    mark = "<html"

    def transfer(self, fname):
        """
        transfer fixture by LiveJournal
        """
        from modules.lj import start
        return self.start_transfer(fname, start, 'lj')

    def test_message(self):
        """
        lj message
        """
        text = self.transfer('msg1.txt')
        assert self.mark not in text

        text = self.transfer('msg2.txt')
        assert self.mark not in text

    def test_no_url(self):
        """
        no url in message
        """
        text = self.transfer('msg3.txt')
        assert self.mark not in text

    def test_last(self):
        """
        another message
        """
        text = self.transfer('msg4.txt')
        assert self.mark not in text
        # print text.encode('cp866', 'ignore')

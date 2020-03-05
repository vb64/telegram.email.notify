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

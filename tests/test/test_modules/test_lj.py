"""Live Journal.

make test T=test_modules/test_lj.py
"""
from . import TestModule


class TestLj(TestModule):
    """
    LiveJournal
    """
    mark = "<html"

    def transfer(self, fname):
        """Transfer fixture by LiveJournal."""
        from modules.lj import start
        return self.start_transfer(fname, start, 'lj')

    def test_lj_message(self):
        """Check lj message."""
        txt = self.transfer('msg1.txt')
        assert self.mark not in txt

        txt = self.transfer('msg2.txt')
        assert self.mark not in txt

    def test_lj_no_url(self):
        """No url in message."""
        text = self.transfer('msg3.txt')
        assert self.mark not in text

    def test_lj_last(self):
        """Another message."""
        text = self.transfer('msg4.txt')
        assert self.mark not in text

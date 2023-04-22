"""Twitter.

make test T=test_default/test_modules/test_twitter.py
"""
from . import TestModule


class TestTwitter(TestModule):
    """Twitter."""

    mark = "Read more at Twitter"

    def transfer(self, fname):
        """Transfer fixture by twitter."""
        from modules.twitter import start
        return self.start_transfer(fname, start, 'twitter')

    def test_message(self):
        """Check message."""
        text = self.transfer('msg1.txt')
        assert self.mark not in text

    def test_twit_happening(self):
        """Check What's happening."""
        txt = self.transfer('msg2.txt')
        assert self.mark not in txt

    def test_twit_newlines_subj(self):
        """New lines in subj."""
        txt = self.transfer('msg3.txt')
        assert self.mark not in txt

    def test_twit_wrong(self):
        """Check no subj."""
        txt = self.transfer('msg4.txt')
        assert self.mark not in txt

    def test_twit_no_term(self):
        """No terminal phrase."""
        txt = self.transfer('msg5.txt')
        assert self.mark not in txt

    def test_twit_06(self):
        """Check msg6.txt."""
        text = self.transfer('msg6.txt')
        assert self.mark not in text

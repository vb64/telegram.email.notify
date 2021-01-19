"""
make test T=test_twitter.py
"""
from . import TestCase


class TestTwitter(TestCase):
    """
    Twitter
    """
    mark = "Read more at Twitter"

    def transfer(self, fname):
        """
        transfer fixture by twitter
        """
        from modules.twitter import start
        return self.start_transfer(fname, start, 'twitter')

    def test_message(self):
        """
        message
        """
        text = self.transfer('msg1.txt')
        assert self.mark not in text

    def test_happening(self):
        """
        What's happening
        """
        text = self.transfer('msg2.txt')
        assert self.mark not in text

    def test_newlines_subj(self):
        """
        new lines in subj
        """
        text = self.transfer('msg3.txt')
        assert self.mark not in text

    def test_wrong(self):
        """
        no subj
        """
        text = self.transfer('msg4.txt')
        assert self.mark not in text

    def test_no_term(self):
        """
        no terminal phrase
        """
        text = self.transfer('msg5.txt')
        assert self.mark not in text

    def test_06(self):
        """
        msg6.txt
        """
        text = self.transfer('msg6.txt')
        assert self.mark not in text
        # print text.decode('utf-8').encode('cp866', 'ignore')

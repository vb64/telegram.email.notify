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

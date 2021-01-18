"""
make test T=test_reddit.py
"""
from . import TestCase


class TestReddit(TestCase):
    """
    Reddit
    """
    mark = "<html"

    def transfer(self, fname):
        """
        transfer fixture by reddit
        """
        from modules.reddit import start
        return self.start_transfer(fname, start, 'reddit')

    def test_message(self):
        """
        reddit message
        """
        text = self.transfer('msg1.txt')
        assert self.mark not in text
        # print text.decode('utf-8').encode('cp866', 'ignore')

    def test_message2(self):
        """
        reddit message2
        """
        text = self.transfer('msg2.txt')
        assert self.mark not in text

    def test_no_link(self):
        """
        reddit message without https://click.redditmail.com/
        """
        text = self.transfer('msg3.txt')
        assert self.mark not in text

    def test_covid(self):
        """
        covid message
        """
        text = self.transfer('msg4.txt')
        assert self.mark not in text

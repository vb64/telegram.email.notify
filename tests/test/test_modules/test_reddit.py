"""
make test T=test_modules/test_reddit.py
"""
from . import TestModule


class TestReddit(TestModule):
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

    def from_eml(self, fname):
        """
        fixture from eml file Reddit
        """
        from modules.reddit import start
        return self.start_eml(fname, start, 'reddit')

    def test_message(self):
        """
        reddit message
        """
        text = self.transfer('msg1.txt')
        assert self.mark not in text

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

    def test_hide(self):
        """
        hide item
        """
        text = self.transfer('msg5.txt')
        assert self.mark not in text

    def test_eml(self):
        """
        md.eml
        """
        from modules import MARKUP

        text = self.from_eml('md.eml')
        assert MARKUP in text

    def test_reddit04(self):
        """
        reddit04.eml
        """
        from modules import MARKUP

        text = self.from_eml('reddit04.eml')
        assert MARKUP in text
        # print text

"""Reddit.

make test T=test_modules/test_reddit.py
"""
from . import TestModule


class TestReddit(TestModule):
    """Reddit."""

    mark = "<html"

    def transfer(self, fname):
        """Transfer fixture by reddit."""
        from modules.reddit import start
        return self.start_transfer(fname, start, 'reddit')

    def from_eml(self, fname):
        """Fixture from eml file Reddit."""
        from modules.reddit import start
        return self.start_eml(fname, start, 'reddit')

    def test_red_message(self):
        """Reddit message."""
        text = self.transfer('msg1.txt')
        assert self.mark not in text

    def test_red_message2(self):
        """Reddit message2."""
        text = self.transfer('msg2.txt')
        assert self.mark not in text

    def test_red_no_link(self):
        """Reddit message without https://click.redditmail.com/ ."""
        text = self.transfer('msg3.txt')
        assert self.mark not in text

    def test_red_covid(self):
        """Covid message."""
        text = self.transfer('msg4.txt')
        assert self.mark not in text

    def test_red_hide(self):
        """Hide item."""
        text = self.transfer('msg5.txt')
        assert self.mark not in text

    def test_red_eml(self):
        """Check md.eml."""
        from modules import MARKUP

        text = self.from_eml('md.eml')
        assert MARKUP in text

    def test_reddit04(self):
        """Check reddit04.eml."""
        from modules import MARKUP

        text = self.from_eml('reddit04.eml')
        assert MARKUP in text

    def test_readmore(self):
        """Check reddit04.eml."""
        from modules.reddit import Section
        sect = Section('First line')
        assert sect.read_more is None
        sect.add_line('Read http://example.com More ')
        assert sect.read_more

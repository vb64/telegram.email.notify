"""Html parser ver2.

make test T=test_default/test_html2text2.py
"""
import os
from . import TestDefault


class TestCaseHtml2text2(TestDefault):
    """Html parser ver2."""

    def test_style(self):
        """Style tag."""
        from html2text2 import convert, Parser

        html = self.get_fixture("msg01.html")
        link = 'http://fishingclub.od.ua/forums/index.php?/topic/'

        text = convert(Parser, html)
        assert text
        assert '#outlook a {padding:0;}' not in text
        assert link not in text

    def test_table(self):
        """Table tags."""
        from html2text2 import convert, Parser

        html = self.get_fixture(os.path.join("galerts", "alert1.txt"))
        text = convert(Parser, html, extract_link=True, html_table=False)
        assert text

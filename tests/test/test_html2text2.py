# -*- coding: utf-8 -*-
"""
make test T=test_html2text2.py
"""
import os

from . import TestCase


class TestCaseHtml2text2(TestCase):
    """
    Html parser ver2
    """
    def test_style(self):
        """
        style tag
        """
        from html2text2 import convert, Parser

        html = self.get_fixture("msg01.html")
        link = 'http://fishingclub.od.ua/forums/index.php?/topic/'

        text = convert(Parser, html)
        assert text
        assert '#outlook a {padding:0;}' not in text
        assert link not in text

    def test_table(self):
        """
        table tags
        """
        from html2text2 import convert, Parser

        html = self.get_fixture(os.path.join("galerts", "alert1.txt"))
        text = convert(Parser, html, extract_link=True, html_table=False)
        assert text

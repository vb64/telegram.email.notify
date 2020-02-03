# -*- coding: utf-8 -*-
"""
Yandex Money
"""
from html2text import HTML2Text


def start(text):
    """
    parse Yandex Money
    """
    parser = HTML2Text()
    parser.ignore_links = True
    return parser.handle(text)

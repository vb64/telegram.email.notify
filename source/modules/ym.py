# -*- coding: utf-8 -*-
"""
Yandex Money
"""
from html2text import convert


def start(text):
    """
    parse Yandex Money
    """
    return convert(text)  # .decode('utf8')

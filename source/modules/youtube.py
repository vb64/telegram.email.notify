# -*- coding: utf-8 -*-
"""
YouTube
"""
from html2text import convert

PREFIX = 'YouTube: '
NBSP = chr(0xC2) + chr(0xA0)


def start(subj, body):
    """
    parse YouTube
    """
    text = convert(body).replace(NBSP, ' ')

    return PREFIX + subj + '\n' + text

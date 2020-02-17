# -*- coding: utf-8 -*-
"""
FaceBook
"""
from html2text import convert

PREFIX = 'FaceBook: '
NBSP = chr(0xC2) + chr(0xA0)


def start(subj, body):
    """
    parse FaceBook
    """
    text = convert(body).replace(NBSP, ' ')

    return PREFIX + subj + '\n' + text

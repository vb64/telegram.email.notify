# -*- coding: utf-8 -*-
"""
FaceBook
"""
from models import SavedSource
from html2text import convert

PREFIX = 'FaceBook: '
NBSP = chr(0xC2) + chr(0xA0)


def start(subj, body):
    """
    parse FaceBook
    """
    SavedSource(label='fb', subject=subj, body=body).put()
    text = convert(body).replace(NBSP, ' ')

    return PREFIX + subj + '\n' + text

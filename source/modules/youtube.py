# -*- coding: utf-8 -*-
"""
YouTube
"""
from models import SavedSource
from html2text import convert

PREFIX = 'YouTube: '
NBSP = chr(0xC2) + chr(0xA0)


def start(subj, body):
    """
    parse YouTube
    """
    SavedSource(label='youtube', subject=subj, body=body).put()
    text = convert(body).replace(NBSP, ' ')

    return PREFIX + subj + '\n' + text

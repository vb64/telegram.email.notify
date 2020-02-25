# -*- coding: utf-8 -*-
"""
YouTube
"""
from models import SavedSource
from html2text import convert

NBSP = chr(0xC2) + chr(0xA0)
MARKUP = '### text_mode markdown\n'
PREFIX = 'YouTube: '
SUBJ_DELIM = ' is live now: '
POST_URL = 'http://www.youtube.com/watch?'


def start(subj, body):
    """
    parse YouTube
    """
    SavedSource(label='youtube', subject=subj, body=body).put()
    if SUBJ_DELIM not in subj:
        return PREFIX + subj + '\n' + convert(body).replace(NBSP, ' ')

    blogger, title = subj.split(SUBJ_DELIM)
    url = ''
    link = title

    for line in body.splitlines():
        if line.startswith(POST_URL):
            url = line
            break

    if url:
        link = "[{}]({})".format(title, url)

    return MARKUP + PREFIX + blogger + '\n' + link

# -*- coding: utf-8 -*-
"""
YouTube
"""
from models import SavedSource
from . import by_subj, MARKUP

LABEL = 'youtube'
SUBJ_LIVE = ' is live now: '
POST_URL = 'http://www.youtube.com/watch?'


def e_live(subj, text):
    """
    'is live now:' in subject
    """
    blogger, title = subj.split(SUBJ_LIVE)
    url = ''
    link = title

    for line in text.splitlines():
        if line.startswith(POST_URL):
            url = line
            break

    if url:
        link = "[{}]({})".format(title, url)
    else:
        SavedSource(label=LABEL, subject=subj, body=text).put()

    return [blogger, '', MARKUP, link]


SUBJ_HANDLERS = [
  ((SUBJ_LIVE, ), e_live),
]


def start(subj, body):
    """
    parse YouTube
    """
    return by_subj(subj, body, body, LABEL, 'YouTube: ', SUBJ_HANDLERS)

# -*- coding: utf-8 -*-
"""
LiveJournal
"""
from models import SavedSource
from . import convert, NBSP, BUTTONS

LABEL = 'lj'
MARK_END = 'https://'


def start(subj, body):
    """
    parse LiveJournal message
    """
    text = convert(body, extract_link=True).replace(NBSP, ' ')
    link = ''
    if MARK_END in text:
        pos = text.index(MARK_END)
        title = text[:pos]
        link = '\n' + BUTTONS + '\n' + "[Читать]({})".format(text[pos:].split()[0])
        text = title
    else:
        SavedSource(label=LABEL, subject=subj, body=body).put()

    return 'LiveJournal: ' + subj + '\n' + text + link

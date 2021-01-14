# -*- coding: utf-8 -*-
"""
Google Alerts
"""
from html2text2 import convert, Parser
from . import by_subj, NBSP

MARK_START_HTML = '<div dir="ltr">'
MARK_SKIP = u"Ещё результаты"


def alert_ru(_subj, text):
    """
    alert with ru language
    """
    return [
      text,
    ]


SUBJ_HANDLERS = [
  (('Оповещение Google ', ), alert_ru),
]


def start(subj, body):
    """
    parse Google Alerts
    """
    text = body
    pos_start = text.index(MARK_START_HTML)
    if pos_start >= 0:
        text = convert(Parser, body[pos_start:].replace(NBSP, ' '), extract_link=True)

    text = by_subj(subj, body, text, 'galerts', u'Оповещение Google\n\n', SUBJ_HANDLERS)

    pos_skip = text.index(MARK_SKIP)
    if pos_skip >= 0:
        text = text[:pos_skip]

    return text

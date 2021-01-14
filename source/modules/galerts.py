# -*- coding: utf-8 -*-
"""
Google Alerts
"""
from html2text import convert
from . import by_subj, NBSP

MARK_START_HTML = '<div dir="ltr">'


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
        text = convert(body[pos_start:]).replace(NBSP, ' ')

    return by_subj(subj, body, text, 'galerts', 'Google Alerts\n\n', SUBJ_HANDLERS)

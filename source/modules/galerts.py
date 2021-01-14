# -*- coding: utf-8 -*-
"""
Google Alerts
"""
import urlparse

from html2text2 import convert, Parser as BaseParser
from . import by_subj, NBSP

MARK_START_HTML = '<div dir="ltr">'
MARK_SKIP = u"Ещё результаты"
MARK_NORELEVANT = u"Пометить как нерелевантный"
MARK_NEWS = u"НОВОСТИ"


class Parser(BaseParser):
    """
    parser class
    """
    def extract_real_link(self, text):  # pylint: disable=no-self-use
        """
        extract real link from google redirects
        """
        if text.startswith('https://www.google.com/url?'):
            return urlparse.parse_qs(urlparse.urlparse(text).query)['url'][0]

        return text


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


def drop_lines(text, marks):
    """
    drop lines starting with any substring from marks
    """
    ret = []
    for line in text.split('\n'):
        if not any([line.startswith(i) for i in marks]):
            ret.append(line)

    return u'\n'.join(ret)


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

    return Parser.drop_newlines(drop_lines(text, [MARK_NORELEVANT, MARK_NEWS]))

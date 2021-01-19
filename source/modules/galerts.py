# -*- coding: utf-8 -*-
"""
Google Alerts
"""
import urlparse

from html2text2 import convert, Parser as BaseParser
from . import by_subj, make_markdown, clear_markdown, NBSP, MARKUP

DELIMETER = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
DROP_RU = [
  u"Пометить как нерелевантный",
  u"НОВОСТИ",
]


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


def alert_ru(subj, text):
    """
    alert with ru language
    """
    pos_skip = text.find(u"Ещё результаты")
    if pos_skip >= 0:
        text = text[:pos_skip]

    lines = []
    for line in text.split('\n'):
        if not any([line.startswith(i) for i in DROP_RU]):
            lines.append(make_markdown(line))

    return [
      MARKUP,
      clear_markdown(subj).decode('utf-8'),
      '',
      Parser.drop_newlines(u'\n'.join(lines)),
    ]


SUBJ_HANDLERS = [
  (('Оповещение Google ', ), alert_ru),
]


def convert_plain_part(subj, body):
    """
    handle plain/text part
    """
    lines = []
    for line in body.split('\n'):
        if line.startswith('<https://www.google.com/url?'):
            line = line.lstrip('<').rstrip('>')
            words = lines[-1].split()
            words[-1] = "[{}]({})".format(words[-1], line)
            lines[-1] = ' '.join(words)
        else:
            lines.append(make_markdown(line))

    return '\n'.join((
      MARKUP,
      clear_markdown(subj), '',
      '\n'.join(lines),
    ))


def start(subj, body):
    """
    parse Google Alerts
    """
    if DELIMETER in body:
        return convert_plain_part(subj, body[:body.index(DELIMETER)])

    text = body
    pos_start = text.find('<div dir="ltr">')
    if pos_start >= 0:
        text = convert(Parser, body[pos_start:].replace(NBSP, ' '), extract_link=True)

    return by_subj(subj, body, text, 'galerts', '', SUBJ_HANDLERS)

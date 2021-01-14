# -*- coding: utf-8 -*-
"""
Google Alerts
"""
import urlparse

from html2text2 import convert, Parser as BaseParser
from . import by_subj, NBSP

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


def is_href(text):
    """
    is text looks like href
    """
    return any([
      text.startswith('https://'),
      text.startswith('http://'),
    ])


def add_href(words, text):
    """
    save text as markdown link
    """
    if not words:
        add_word(words, text)
        return

    last_word = words[-1]
    if last_word[1]:  # already link
        add_word(words, text)
        return

    words[-1] = (u"[{}]({})".format(last_word[0], text), True)


def add_word(words, text):
    """
    save simple text
    """
    words.append((text, False))  # clear *_


def make_markdown(text):
    """
    embed url as markdown links
    """
    result = []
    for word in text.split():
        if is_href(word):
            add_href(result, word)
        else:
            add_word(result, word)

    return ' '.join([i[0] for i in result])


def alert_ru(subj, text):
    """
    alert with ru language
    """
    pos_skip = text.index(u"Ещё результаты")
    if pos_skip >= 0:
        text = text[:pos_skip]

    lines = []
    for line in text.split('\n'):
        if not any([line.startswith(i) for i in DROP_RU]):
            lines.append(make_markdown(line))

    return [
      subj.decode('utf-8'),
      '',
      Parser.drop_newlines(u'\n'.join(lines)),
    ]


SUBJ_HANDLERS = [
  (('Оповещение Google ', ), alert_ru),
]


def start(subj, body):
    """
    parse Google Alerts
    """
    text = body
    pos_start = text.index('<div dir="ltr">')
    if pos_start >= 0:
        text = convert(Parser, body[pos_start:].replace(NBSP, ' '), extract_link=True)

    return by_subj(subj, body, text, 'galerts', '', SUBJ_HANDLERS)

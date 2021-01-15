# -*- coding: utf-8 -*-
"""
LiveJournal
"""
from html2text2 import convert, Parser as BaseParser
from . import make_markdown, clear_markdown, MARKUP

DROP_IN = [
  u'.livejournal.com?utm_source=',
  u'LiveJournal Newsletter ',
  u"Вечерний ЖЖ ",
]


class Parser(BaseParser):
    """
    parser class for LJ
    """
    def extract_real_link(self, text):  # pylint: disable=no-self-use
        """
        extract part of link without ru symbols
        """
        index = text.find('?utm_source=')
        if index > 0:
            return text[:index]

        return text


def start(subj, body):
    """
    parse LiveJournal message
    """
    text = convert(Parser, body, extract_link=True)
    pos_end = text.find(u"Ещё больше интересного Подписывайтесь")
    if pos_end > 0:
        text = text[:pos_end]

    lines = []
    for line in text.split('\n'):
        if not any([i in line for i in DROP_IN]):
            lines.append(make_markdown(line))

    return u'\n'.join((
      u'LiveJournal: ' + clear_markdown(subj).decode('utf-8'),
      MARKUP,
      Parser.drop_newlines(u'\n'.join(lines)),
    ))

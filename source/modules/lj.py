# -*- coding: utf-8 -*-
"""
LiveJournal
"""
from html2text2 import convert, Parser
from . import make_markdown, clear_markdown, MARKUP

DROP_IN = [
  u'.livejournal.com?utm_source=',
  u'LiveJournal Newsletter ',
]


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

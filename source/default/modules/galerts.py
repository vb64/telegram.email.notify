# pylint: disable=W0223
"""Google Alerts."""
from urllib.parse import parse_qs, urlparse

from html2text2 import Parser as BaseParser
from . import by_subj, make_markdown, clear_markdown, MARKUP

DELIMETER = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
DROP_RU = [
  "Пометить как нерелевантный",
  "[image:",
  "<https://www.google.ru/alerts"
]
TRASH = [
  "Twitter]\nПометить\nкак нерелевантный",
]


class Parser(BaseParser):
    """Parser class."""

    def extract_real_link(self, text):
        """Extract real link from google redirects."""
        if text.startswith('https://www.google.com/url?'):
            return parse_qs(urlparse(text).query)['url'][0].encode('utf-8')

        return text.encode('utf-8')


def clear_trash(text):
    """Remove trash items from text."""
    for i in TRASH:
        text = text.replace(i, '')

    return text


def alert_ru(subj, text):
    """Alert with ru language."""
    pos_skip = text.find("Ещё результаты")
    if pos_skip >= 0:
        text = text[:pos_skip]

    lines = []
    for line in text.split('\n'):
        if not any([line.startswith(i) for i in DROP_RU]):  # pylint: disable=use-a-generator
            lines.append(make_markdown(line))

    return [
      MARKUP,
      clear_markdown(subj),
      '',
      clear_trash(Parser.drop_newlines('\n'.join(handle_lines(lines)))),
    ]


SUBJ_HANDLERS = [
  (('Оповещение Google ', ), alert_ru),
]


def handle_lines(text_lines):
    """Handle text lines."""
    lines = []
    for line in text_lines:
        if line.startswith('<https://www.google.com/url?'):
            line = line.lstrip('<').rstrip('>')
            words = lines[-1].split()
            words[-1] = "[{}]({})".format(words[-1], line)
            lines[-1] = ' '.join(words)
        else:
            lines.append(make_markdown(clear_markdown(line)))

    return lines


def convert_plain_part(subj, body):
    """Handle plain/text part."""
    lines = handle_lines(body.split('\n'))

    return '\n'.join((
      MARKUP,
      clear_markdown(subj), '',
      clear_trash('\n'.join(lines)),
    ))


def start(subj, body):
    """Parse Google Alerts."""
    if DELIMETER in body:
        return convert_plain_part(subj, body[:body.index(DELIMETER)])

    text = body
    pos_start = text.find('<div dir="ltr">')
    if pos_start >= 0:
        parser = Parser(True, True)
        parser.feed(body[pos_start:])
        parser.close()
        text = parser.text()

    return by_subj(subj, body, text, 'galerts', '', SUBJ_HANDLERS)

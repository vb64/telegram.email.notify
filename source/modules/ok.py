# -*- coding: utf-8 -*-
"""
Odnoklassniki.ru
"""
from html2text import convert
from . import by_subj, BUTTONS, NBSP

LABEL = 'ok'

SUBJ_POST = 'Пока вас не было'
SUBJ_PRESENT = 'вам подарок'


def e_message(_subj, text):
    """
    message
    """
    return [convert(text).replace(NBSP, ' ')]


def e_present(subj, text):
    """
    present
    """
    link = ""
    lines = iter(text.splitlines())
    for line in lines:
        if ('https://ok.ru/?' in line) and ('lookPresent' in line):
            link = "[Посмотреть]({})".format(line)
            break

    return [subj, '', BUTTONS, link]


SUBJ_HANDLERS = [
  ((SUBJ_POST, ), e_message),
  ((SUBJ_PRESENT, ), e_present),
]


def start(subj, body):
    """
    parse Odnoklassniki.ru
    """
    return by_subj(subj, body, body, LABEL, 'Одноклассники: ', SUBJ_HANDLERS)

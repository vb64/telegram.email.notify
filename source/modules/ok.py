# -*- coding: utf-8 -*-
"""
Odnoklassniki.ru
"""
from html2text import convert
from . import is_present, by_subj, BUTTONS, NBSP

LABEL = 'ok'

SUBJ_POST = 'Пока вас не было'
SUBJ_PRESENT = 'вам подарок'

BUTT_VIWEW = "[Посмотреть]({})"

MARK_PHOTO = [' добавил', ' фото']
MARK_PHOTO_REF = '.PHOTO_ADDED'
MARK_PROFILE_REF = 'https://ok.ru/profile/'


def e_message(_subj, text):
    """
    message
    """
    txt = convert(text, extract_link=True).replace(NBSP, ' ')

    if is_present(MARK_PHOTO + [MARK_PHOTO_REF, MARK_PROFILE_REF], txt):
        actor = txt[:txt.index(MARK_PROFILE_REF)]
        actor = actor[actor.rindex(SUBJ_POST) + len(SUBJ_POST):].strip() + ' новое фото'
        link = ''
        for word in txt.split():
            if is_present([MARK_PROFILE_REF, MARK_PHOTO_REF], word):
                link = BUTT_VIWEW.format(word)
                break

        return [actor, '', BUTTONS, link]

    return [txt]


def e_present(subj, text):
    """
    present
    """
    link = ""
    lines = iter(text.splitlines())
    for line in lines:
        if is_present(['https://ok.ru/?', 'lookPresent'], line):
            link = BUTT_VIWEW.format(line)
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

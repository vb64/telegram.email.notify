# -*- coding: utf-8 -*-
"""
FaceBook
"""
from models import SavedSource
from . import by_subj, BUTTONS

LABEL = 'fb'
MARK_VIEW = 'Посмотреть на Facebook'
SUBJ_COMMENT = 'Посмотрите комментарий'


def read_citate(lines):
    """
    read citate from iterator
    """
    ret = []
    for line in lines:
        next_line = None
        if line == 'С уважением,':
            next_line = next(lines)
            if next_line == 'Команда Facebook':
                break

        ret.append(line.strip('"'))
        if next_line is not None:
            ret.append(next_line.strip('"'))

    return '\n'.join(ret)


def e_comment(subj, text):
    """
    comment
    """
    link = ''
    title = ''
    citate = ''

    lines = iter(text.splitlines())
    for line in lines:
        if line.startswith(MARK_VIEW):
            link = "[{}]({})".format(MARK_VIEW, next(lines))
        elif line.startswith(SUBJ_COMMENT):
            title = line
        elif line.startswith('Посетить группу'):
            citate = read_citate(lines)
            break

    if not all([link, title, citate]):
        SavedSource(label=LABEL, subject=subj, body=text).put()

    return [title, '', citate, BUTTONS, link]


SUBJ_HANDLERS = [
  ((SUBJ_COMMENT, ), e_comment),
  # (('добавил', ' новое фото'), e_post),
  # (('Посмотрите новую публикацию', ), e_post),
  # (('У вас ', ' новых рекомендаций'), e_post),
]


def start(subj, body):
    """
    parse FaceBook
    """
    SavedSource(label='fb_all', subject=subj, body=body).put()
    return by_subj(subj, body, body, LABEL, 'FaceBook: ', SUBJ_HANDLERS)

# -*- coding: utf-8 -*-
"""
FaceBook
"""
from models import SavedSource
from . import by_subj, BUTTONS

LABEL = 'fb'
MARK_VIEW = 'Посмотреть на Facebook'
MARK_ACCEPT = 'Подтвердить запрос'

SUBJ_COMMENT = 'Посмотрите комментарий'
SUBJ_POST = 'Посмотрите новую публикацию'
SUBJ_FRIEND = 'хочет стать вашим другом на Facebook'
SUBJ_FRIEND1 = 'запрос на добавление в друзья'
SUBJ_PHOTO = 'Посмотрите новое фото'


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


def get_handler(prefix, mark):
    """
    closure for subj handler
    """
    def e_post(subj, text):
        """
        post
        """
        link = ''
        title = ''
        citate = ''

        lines = iter(text.splitlines())
        for line in lines:
            if line.startswith(mark):
                link = "[{}]({})".format(mark, next(lines))
            elif line.startswith(prefix):
                title = line
            elif line in ['Посетить группу', 'Читать публикацию']:
                citate = read_citate(lines)
                break

        if not all([link, title]):
            SavedSource(label=LABEL, subject=subj, body=text).put()

        return [title, '', citate, BUTTONS, link]

    return e_post


def e_photo(subj, _text):
    """
    photo
    """
    return [subj]


def e_recommend(subj, _text):
    """
    recommendation
    """
    return [subj]


SUBJ_HANDLERS = [
  ((SUBJ_COMMENT, ), get_handler(SUBJ_COMMENT, MARK_VIEW)),
  ((SUBJ_POST, ), get_handler(SUBJ_POST, MARK_VIEW)),
  ((SUBJ_FRIEND, ), get_handler(SUBJ_FRIEND, MARK_ACCEPT)),
  ((SUBJ_FRIEND1, ), get_handler(SUBJ_FRIEND1, MARK_ACCEPT)),
  ((SUBJ_PHOTO, ), get_handler(SUBJ_PHOTO, MARK_VIEW)),
  (('добавил', ' новое фото'), e_photo),
  (('У вас ', ' новых рекомендаций'), e_recommend),
]


def start(subj, body):
    """
    parse FaceBook
    """
    return by_subj(subj, body, body, LABEL, 'FaceBook: ', SUBJ_HANDLERS)

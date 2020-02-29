# -*- coding: utf-8 -*-
"""
FaceBook
"""
from models import SavedSource
from . import by_subj, BUTTONS

LABEL = 'fb'
MARK_VIEW = 'Посмотреть на Facebook'
SUBJ_COMMENT = 'Посмотрите комментарий'
SUBJ_POST = 'Посмотрите новую публикацию'


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


def get_handler(prefix):
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
            if line.startswith(MARK_VIEW):
                link = "[{}]({})".format(MARK_VIEW, next(lines))
            elif line.startswith(prefix):
                title = line
            elif line in ['Посетить группу', 'Читать публикацию']:
                citate = read_citate(lines)
                break

        if not all([link, title, citate]):
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
  ((SUBJ_COMMENT, ), get_handler(SUBJ_COMMENT)),
  ((SUBJ_POST, ), get_handler(SUBJ_POST)),
  (('добавил', ' новое фото'), e_photo),
  (('У вас ', ' новых рекомендаций'), e_recommend),
]


def start(subj, body):
    """
    parse FaceBook
    """
    SavedSource(label='fb_all', subject=subj, body=body).put()
    return by_subj(subj, body, body, LABEL, 'FaceBook: ', SUBJ_HANDLERS)

# -*- coding: utf-8 -*-
"""
FaceBook
"""
from . import BUTTONS

DELIMETER = '========================================'
MARK_VIEW = 'Посмотреть на Facebook'
MARK_HI = 'Здравствуйте, '


def extract_link(text):
    """
    extract link to fb post
    """
    if not text.startswith(MARK_VIEW):
        return ''

    link = text.split('\n')[1]
    return '\n'.join((
      '',
      BUTTONS,
      "[{}]({})".format(MARK_VIEW, link),
    ))


def extract_text(text):
    """
    extract value from text part
    """
    lines = text.split('\n')
    start_indx = 0
    end_indx = len(lines) - 1

    for i, line in enumerate(lines):
        if line.startswith('"'):
            start_indx = i
            break

    for i, line in enumerate(lines[start_indx:]):
        if line.endswith('"'):
            end_indx = start_indx + i
            break

    if start_indx == end_indx:
        lines[start_indx] = lines[start_indx][1:-1]
        result = [lines[start_indx]]
    else:
        lines[start_indx] = lines[start_indx][1:]
        lines[end_indx] = lines[end_indx][:-1]
        result = lines[start_indx:end_indx]

    return '\n'.join(result)


def start(subj, body):
    """
    parse FaceBook
    """
    parts = body.split(DELIMETER)
    text = ''.join((
      subj,
      '\n\n',
      extract_text(parts[2].strip()),
      extract_link(parts[1].strip()),
    ))

    return text.decode('utf-8')

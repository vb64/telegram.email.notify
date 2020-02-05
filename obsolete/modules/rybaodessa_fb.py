# -*- coding: utf-8 -*-
from . import ecode

mark = "Нравится Комментарий "


def start(text):
    source = ecode(text)
    i = source.find(mark)
    if i == -1:
        return source

    return source[:i]

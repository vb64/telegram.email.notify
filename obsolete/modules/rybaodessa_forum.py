# -*- coding: utf-8 -*-
from . import ecode, remove_line_with, remove_new_lines

sign = "Одесский Клуб Рыболовов: "
mark1 = "Ответ в теме "
mark2 = "Перейти к сообщению"
mark3 = " только что ответил в теме, на которую Вы подписались"
mark4 = "но Вы не будете получать уведомления, пока снова не посетите форум."


def start(text):
    source = ecode(text)
    if mark1 not in source:
        return variant2(source)

    i = source.find(mark3)
    if i == -1:
        return source

    i = source.rfind('\n', 0, i)
    if i == -1:
        return source

    txt = source[i:]
    i = txt.find(mark4)
    if i == -1:
        return remove_new_lines(txt)

    # print "#txt", txt[:i + len(mark4)].decode('utf-8')
    return remove_new_lines(txt[:i + len(mark4)])


def variant2(source):
    i = source.find(mark2)
    if i == -1:
        return source

    txt = remove_line_with(source[:i - 1], " Здравствуйте, VinsT!")
    txt = remove_line_with(txt, " опубликовал комментарий в тему, ")

    return remove_new_lines("{}{}".format(sign, txt))

# -*- coding: utf-8 -*-
"""
Yandex Money
"""
from html2text import convert

EVNT_PAY = 'Вы заплатили с карты Яндекс.Денег'
EVNT_CASH = 'Вы сняли наличные с карты Яндекс.Денег'

MARK_CARD = 'Карта '
MARK_TARGET = 'Назначение платежа '
MARK_DATE = 'Дата и время '
MARK_SUMM = 'Сколько списано '
MARK_PLACE = 'Страна и город '
MARK_AVAIL = 'Доступно '
MARK_HIST1 = 'Запись о платеже хранится '
MARK_BANK = 'Банкомат '
MARK_CASH = 'Выданная сумма '
MARK_COMIS = 'Комиссия за снятие '
MARK_CURR = 'Сумма в валюте операции '
MARK_LIMIT = 'В этом месяце вы можете снять '
MARK_HIST2 = 'Запись обо всех операциях '


def event_cash(text):
    """
    event cash out
    """
    pos_card = text.index(MARK_CARD)
    pos_bank = text.index(MARK_BANK)
    pos_date = text.index(MARK_DATE)
    pos_cash = text.index(MARK_CASH)
    pos_comis = text.index(MARK_COMIS)
    pos_curr = text.index(MARK_CURR)
    pos_place = text.index(MARK_PLACE)
    pos_avail = text.index(MARK_AVAIL)
    pos_limit = text.index(MARK_LIMIT)
    pos_hist = text.index(MARK_HIST2)

    return '\n'.join([
      EVNT_CASH, '',
      text[pos_card:pos_bank],
      text[pos_bank:pos_date],
      text[pos_date:pos_cash],
      text[pos_cash:pos_comis],
      text[pos_comis:pos_curr],
      text[pos_place:pos_avail],
      text[pos_avail:pos_limit],
      text[pos_limit:pos_hist],
    ])


def event_pay(text):
    """
    event payment
    """
    pos_card = text.index(MARK_CARD)
    pos_target = text.index(MARK_TARGET)
    pos_date = text.index(MARK_DATE)
    pos_summ = text.index(MARK_SUMM)
    pos_place = text.index(MARK_PLACE)
    pos_avail = text.index(MARK_AVAIL)
    pos_hist = text.index(MARK_HIST1)

    return '\n'.join([
      EVNT_PAY, '',
      text[pos_card:pos_target],
      text[pos_target:pos_date],
      text[pos_date:pos_summ],
      text[pos_summ:pos_place],
      text[pos_place:pos_avail],
      text[pos_avail:pos_hist],
    ])


def start(html):
    """
    parse Yandex Money
    """
    text = convert(html)
    if isinstance(text, unicode):
        text = text.encode('utf8')

    result = text

    if text.find(EVNT_PAY) == 0:
        result = event_pay(text)
    elif text.find(EVNT_CASH) == 0:
        result = event_cash(text)

    return result

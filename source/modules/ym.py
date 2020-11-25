# -*- coding: utf-8 -*-
"""
Yandex Money
"""
from html2text import convert
from . import by_subj, NBSP

MARK_CARD = 'Карта '
MARK_TARGET = 'Назначение платежа'
MARK_DATE = 'Дата и время'
MARK_SUMM = 'Сколько списано'
MARK_PLACE = 'Страна и город'
MARK_AVAIL = 'Доступно '
MARK_HIST1 = 'Запись о платеже хранится'
MARK_BANK = 'Банкомат'
MARK_CASH = 'Выданная сумма'
MARK_COMIS = 'Комиссия за снятие'
MARK_CURR = 'Сумма в валюте операции'
MARK_LIMIT = 'В этом месяце вы можете снять'
MARK_HIST2 = 'Запись обо всех операциях'
MARK_TRANS_IN = 'Пополнение через'
MARK_TRANS_SUM = 'Сумма'
MARK_HIST3 = 'Все детали платежа'
MARK_COMMENT = 'Комментарий'
MARK_BONUS_TOTAL = 'Баллы баланс'
MARK_BONUS_WEEK = 'За неделю вы заработали'
MARK_HIST4 = 'Где получать баллы'
MARK_TRANS_OUT = 'Назначение платежа'
MARK_TRANS_OUT_SUM = 'Со счета списано'
MARK_COMIS_YM = 'Комиссия ЮMoney'
MARK_SUMM_WALLET = 'Списано'
MARK_HIST5 = 'Все детали пополнения'


def e_paywallet(subj, text):
    """
    transfer out
    """
    pos_target = text.index(MARK_TARGET)
    pos_date = text.index(MARK_DATE)
    pos_sum = text.index(MARK_SUMM_WALLET)
    pos_avail = text.index(MARK_AVAIL)
    pos_hist = text.index(MARK_HIST3)

    if MARK_COMIS_YM in text:
        pos_com = text.index(MARK_COMIS_YM)
        fields = [
          text[pos_sum:pos_com],
          text[pos_com:pos_avail],
        ]
    else:
        fields = [text[pos_sum:pos_avail]]

    return [
      subj, '',
      text[pos_target:pos_date],
      text[pos_date:pos_sum],
    ] + fields + [
      text[pos_avail:pos_hist],
    ]


def e_paycard(subj, text):
    """
    Yandex card payment
    """
    pos_target = text.index(MARK_TARGET)
    pos_date = text.index(MARK_DATE)
    pos_sum = text.index(MARK_TRANS_SUM)
    pos_com = text.index(MARK_COMIS_YM)
    pos_hist = text.index(MARK_HIST3)

    return [
      subj, '',
      text[pos_target:pos_date],
      text[pos_date:pos_sum],
      text[pos_sum:pos_com],
      text[pos_com:pos_hist],
    ]


def e_transf_out(subj, text):
    """
    transfer out
    """
    pos_trans = text.index(MARK_TRANS_OUT)
    pos_date = text.index(MARK_DATE)
    pos_sum = text.index(MARK_TRANS_OUT_SUM)
    pos_avail = text.index(MARK_AVAIL)
    pos_hist = text.index(MARK_HIST3)

    return [
      subj, '',
      text[pos_trans:pos_date],
      text[pos_date:pos_sum],
      text[pos_sum:pos_avail],
      text[pos_avail:pos_hist],
    ]


def e_week(subj, text):
    """
    week note
    """
    pos_total = text.index(MARK_BONUS_TOTAL)
    pos_week = text.index(MARK_BONUS_WEEK)
    pos_hist = text.index(MARK_HIST4)

    return [
      subj, '',
      text[pos_total:pos_week],
      text[pos_week:pos_hist],
    ]


def e_transf_in(subj, text):
    """
    transfer income
    """
    pos_date = text.index(MARK_DATE)
    pos_sum = text.index(MARK_TRANS_SUM)
    pos_avail = text.index(MARK_AVAIL)
    pos_hist = text.index(MARK_HIST3)

    if MARK_COMMENT in text:
        pos_note = text.index(MARK_COMMENT)
        fields = [
          text[pos_sum:pos_note],
          text[pos_note:pos_avail],
        ]
    else:
        fields = [text[pos_sum:pos_avail]]

    return [
      subj, '',
      text[pos_date:pos_sum],
    ] + fields + [
      text[pos_avail:pos_hist],
    ]


def e_income1(subj, text):
    """
    income1
    """
    pos_date = text.index(MARK_DATE)
    pos_trans = text.index(MARK_TRANS_IN)
    pos_sum = text.index(MARK_TRANS_SUM)
    pos_avail = text.index(MARK_AVAIL)
    pos_hist = text.index(MARK_HIST5)

    return [
      subj, '',
      text[pos_date:pos_trans], text[pos_trans:pos_sum],
      text[pos_sum:pos_avail], text[pos_avail:pos_hist],
    ]


def e_income(subj, text):
    """
    income
    """
    pos_date = text.index(MARK_DATE)
    pos_trans = text.index(MARK_TRANS_IN)
    pos_sum = text.index(MARK_TRANS_SUM)
    pos_avail = text.index(MARK_AVAIL)
    pos_hist = text.index(MARK_HIST3)

    return [
      subj, '',
      text[pos_date:pos_trans],
      text[pos_trans:pos_sum],
      text[pos_sum:pos_avail],
      text[pos_avail:pos_hist],
    ]


def e_cashback(subj, _text):
    """
    cashback
    """
    return [
      'Напоминание о кэшбэк', '', subj,
    ]


def e_cash(subj, text):
    """
    cash out
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

    return [
      subj, '',
      text[pos_card:pos_bank],
      text[pos_bank:pos_date],
      text[pos_date:pos_cash],
      text[pos_cash:pos_comis],
      text[pos_comis:pos_curr],
      text[pos_place:pos_avail],
      text[pos_avail:pos_limit],
      text[pos_limit:pos_hist],
    ]


def e_pay(subj, text):
    """
    payment
    """
    pos_card = text.index(MARK_CARD)
    pos_target = text.index(MARK_TARGET)
    pos_date = text.index(MARK_DATE)
    pos_summ = text.index(MARK_SUMM)
    pos_place = text.index(MARK_PLACE)
    pos_avail = text.index(MARK_AVAIL)
    pos_hist = text.index(MARK_HIST1)

    return [
      subj, '',
      text[pos_card:pos_target],
      text[pos_target:pos_date],
      text[pos_date:pos_summ],
      text[pos_summ:pos_place],
      text[pos_place:pos_avail],
      text[pos_avail:pos_hist],
    ]


SUBJ_HANDLERS = [
  (('Вы заплатили с карты ЮMoney', ), e_pay),
  (('Вы заплатили с банковской карты', ), e_paycard),
  (('Вы заплатили из кошелька', ), e_paywallet),
  (('Вы сняли наличные с карты', ), e_cash),
  (('Кэшбэк ', ), e_cashback),
  (('Ваш счет ', ' пополнен'), e_income),
  (('На ваш счет ', ' поступил перевод'), e_transf_in),
  (('ваши баллы и скидки за неделю', ), e_week),
  (('Вы заплатили со счета ', ), e_transf_out),
  (('Ваш кошелек ', ' пополнен'), e_income1),
]


def start(subj, body):
    """
    parse Yandex Money
    """
    return by_subj(subj, body, convert(body).replace(NBSP, ' '), 'ym', 'ЮMoney: ', SUBJ_HANDLERS)

# -*- coding: utf-8 -*-
"""
Yandex Money
"""
from html2text import convert

EVNT_PAY = 'Вы заплатили с карты Яндекс.Денег'
EVNT_PAY_CARD = 'Вы заплатили с банковской карты'
EVNT_PAY_WALLET = 'Вы заплатили из кошелька'
EVNT_CASH = 'Вы сняли наличные с карты Яндекс.Денег'
EVNT_CASHBACK = 'Кэшбэк '
EVNT_INCOME1 = 'Ваш счет '
EVNT_INCOME2 = ' пополнен'
EVNT_TRANS_IN1 = 'На ваш счет '
EVNT_TRANS_IN2 = ' поступил перевод'
EVNT_WEEK = 'ваши баллы и скидки за неделю'
EVNT_TRANS_OUT = 'Вы заплатили со счета '

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
MARK_TRANS_IN = 'Пополнение через '
MARK_TRANS_SUM = 'Сумма '
MARK_HIST3 = 'Все детали платежа'
MARK_COMMENT = 'Комментарий '
MARK_BONUS_TOTAL = 'Баллы баланс '
MARK_BONUS_WEEK = 'За неделю вы заработали '
MARK_HIST4 = 'Где получать баллы '
MARK_TRANS_OUT = 'Назначение платежа '
MARK_TRANS_OUT_SUM = 'Со счета списано '
MARK_COMIS_YM = 'Комиссия Яндекс.Денег '
MARK_SUMM_WALLET = 'Списано '


def event_paywallet(subj, text):
    """
    event transfer out
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

    return '\n'.join([
      subj, '',
      text[pos_target:pos_date],
      text[pos_date:pos_sum],
    ] + fields + [
      text[pos_avail:pos_hist],
    ])


def event_paycard(subj, text):
    """
    event transfer out
    """
    pos_target = text.index(MARK_TARGET)
    pos_date = text.index(MARK_DATE)
    pos_sum = text.index(MARK_TRANS_SUM)
    pos_com = text.index(MARK_COMIS_YM)
    pos_hist = text.index(MARK_HIST3)

    return '\n'.join([
      subj, '',
      text[pos_target:pos_date],
      text[pos_date:pos_sum],
      text[pos_sum:pos_com],
      text[pos_com:pos_hist],
    ])


def event_transf_out(subj, text):
    """
    event transfer out
    """
    pos_trans = text.index(MARK_TRANS_OUT)
    pos_date = text.index(MARK_DATE)
    pos_sum = text.index(MARK_TRANS_OUT_SUM)
    pos_avail = text.index(MARK_AVAIL)
    pos_hist = text.index(MARK_HIST3)

    return '\n'.join([
      subj, '',
      text[pos_trans:pos_date],
      text[pos_date:pos_sum],
      text[pos_sum:pos_avail],
      text[pos_avail:pos_hist],
    ])


def event_week(subj, text):
    """
    event week note
    """
    pos_total = text.index(MARK_BONUS_TOTAL)
    pos_week = text.index(MARK_BONUS_WEEK)
    pos_hist = text.index(MARK_HIST4)

    return '\n'.join([
      subj, '',
      text[pos_total:pos_week],
      text[pos_week:pos_hist],
    ])


def event_transf_in(subj, text):
    """
    event transfer income
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

    return '\n'.join([
      subj, '',
      text[pos_date:pos_sum],
    ] + fields + [
      text[pos_avail:pos_hist],
    ])


def event_income(subj, text):
    """
    event income
    """
    pos_date = text.index(MARK_DATE)
    pos_trans = text.index(MARK_TRANS_IN)
    pos_sum = text.index(MARK_TRANS_SUM)
    pos_avail = text.index(MARK_AVAIL)
    pos_hist = text.index(MARK_HIST3)

    return '\n'.join([
      subj, '',
      text[pos_date:pos_trans],
      text[pos_trans:pos_sum],
      text[pos_sum:pos_avail],
      text[pos_avail:pos_hist],
    ])


def event_cashback(subj, _text):
    """
    event cashback
    """
    return '\n'.join([
      'Напоминание о кэшбэк', '', subj,
    ])


def event_cash(subj, text):
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
      subj, '',
      text[pos_card:pos_bank],
      text[pos_bank:pos_date],
      text[pos_date:pos_cash],
      text[pos_cash:pos_comis],
      text[pos_comis:pos_curr],
      text[pos_place:pos_avail],
      text[pos_avail:pos_limit],
      text[pos_limit:pos_hist],
    ])


def event_pay(subj, text):
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
      subj, '',
      text[pos_card:pos_target],
      text[pos_target:pos_date],
      text[pos_date:pos_summ],
      text[pos_summ:pos_place],
      text[pos_place:pos_avail],
      text[pos_avail:pos_hist],
    ])


def start(subj, body):
    """
    parse Yandex Money
    """
    text = convert(body)
    result = subj + '\n' + text

    if EVNT_PAY in subj:
        result = event_pay(subj, text)
    elif EVNT_PAY_CARD in subj:
        result = event_paycard(subj, text)
    elif EVNT_PAY_WALLET in subj:
        result = event_paywallet(subj, text)
    elif EVNT_CASH in subj:
        result = event_cash(subj, text)
    elif EVNT_CASHBACK in subj:
        result = event_cashback(subj, text)
    elif (EVNT_INCOME1 in subj) and (EVNT_INCOME2 in subj):
        result = event_income(subj, text)
    elif (EVNT_TRANS_IN1 in subj) and (EVNT_TRANS_IN1 in subj):
        result = event_transf_in(subj, text)
    elif EVNT_WEEK in subj:
        result = event_week(subj, text)
    elif EVNT_TRANS_OUT in subj:
        result = event_transf_out(subj, text)

    return 'Яндекс.Деньги: ' + result

# -*- coding: utf-8 -*-
"""
Yandex Money
"""
from html2text2 import convert, Parser
from . import is_present, by_subj, NBSP

MARK_CARD = u'Карта '
MARK_TARGET = u'Назначение платежа'
MARK_DATE = u'Дата и время'
MARK_SUMM = u'Сколько списано'
MARK_PLACE = u'Страна и город'
MARK_AVAIL = u'Доступно '
MARK_HIST1 = u'Запись о платеже хранится'
MARK_BANK = u'Банкомат'
MARK_CASH = u'Выданная сумма'
MARK_COMIS = u'Комиссия за снятие'
MARK_CURR = u'Сумма в валюте операции'
MARK_LIMIT = u'В этом месяце вы можете снять'
MARK_HIST2 = u'Запись обо всех операциях'
MARK_TRANS_IN = u'Пополнение через'
MARK_TRANS_SUM = u'Сумма'
MARK_HIST3 = u'Все детали платежа'

MARK_COMIS_YM = u'Комиссия ЮMoney'


def e_paywallet(subj, text):
    """
    transfer out
    """
    pos_target = text.index(MARK_TARGET)
    pos_date = text.index(MARK_DATE)
    pos_sum = text.index(u'Списано')
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
    pos_trans = text.index(u'Назначение платежа')
    pos_date = text.index(MARK_DATE)
    pos_sum = text.index(u'Со счета списано')
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
    pos1 = text.index(u'баланс на ')
    pos2 = text.index(u'Где получать баллы')

    return [
      subj, '',
      text[pos1:pos2],
    ]


def e_transf_in(subj, text):
    """
    transfer income
    """
    pos_date = text.index(MARK_DATE)
    pos_sum = text.index(MARK_TRANS_SUM)
    pos_avail = text.index(MARK_AVAIL)
    pos_hist = text.index(MARK_HIST3)
    comment = u'Комментарий'

    if comment in text:
        pos_note = text.index(comment)
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
    pos_hist = text.index(u'Все детали пополнения')

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
      u'Напоминание о кэшбэк', '', subj,
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
  ((u'Вы заплатили с карты ЮMoney', ), e_pay),
  ((u'Вы заплатили с банковской карты', ), e_paycard),
  ((u'Вы заплатили из кошелька', ), e_paywallet),
  ((u'Вы сняли наличные с карты', ), e_cash),
  ((u'Кэшбэк ', ), e_cashback),
  ((u'Ваш счет ', u' пополнен'), e_income),
  ((u'На ваш счет ', u' поступил перевод'), e_transf_in),
  ((u'ваши баллы и скидки за неделю', ), e_week),
  ((u'Вы заплатили со счета ', ), e_transf_out),
  ((u'Ваш кошелек ', u' пополнен'), e_income1),
]
SUBJ_ONLY = [
  (u'Информация о платеже',),
  (u'Статус распоряжения:',),
  (u'Как насчёт вашей подписки',),
  (u'Получайте ', u'годовых'),
  (u'Переводы с комиссией',),
  (u'сундук с призами',),
  (u'На всякий случай:',),
  (u'Несколько вопросов',),
  (u'Получите подарок',),
  (u'Выиграйте',),
  (u'Повышенный кэшбэк',),
  (u'Получайте кэшбэк',),
  (u'Списание средств',),
  (u'поступили денежные средства',),
  (u'о важном',),
  (u'найдёт для вас кэшбэк',),
  (u'Сохраните свои деньги',),
  (u'Вход', u'от имени клиента'),
  (u'Транзакция по банковской карте',),
  (u'Автоплатежи',),
  (u'Получите бонус',),
  (u'Поступление зарплаты',),
  (u'Инвестируйте',),
  (u'возврат по операции',),
]


def start(subj, body):
    """
    parse Yandex Money
    """
    title = u'ЮMoney: '
    subj = subj.decode('utf-8')

    for marks in SUBJ_ONLY:
        if is_present(marks, subj):
            return title + subj

    return by_subj(
      subj,
      body,
      convert(Parser, body.replace(NBSP, ' ')),
      'ym',
      title,
      SUBJ_HANDLERS
    )

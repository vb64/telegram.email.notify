"""Yandex Money."""
from html2text2 import convert, Parser
from modutil import is_present, by_subj, NBSP

MARK_CARD = 'Карта '
MARK_TARGET = 'Назначение платежа'
MARK_DATE = 'Дата и время'
MARK_PLACE = 'Страна и город'
MARK_AVAIL = 'Доступно '
MARK_TRANS_IN = 'Пополнение через'
MARK_TRANS_SUM = 'Сумма'
MARK_HIST = 'Все детали платежа'
MARK_COMIS = 'Комиссия ЮMoney'


def e_paywallet(subj, text):
    """Transfer out."""
    pos_target = text.index(MARK_TARGET)
    pos_date = text.index(MARK_DATE)
    pos_sum = text.index('Списано')
    pos_avail = text.index(MARK_AVAIL)
    pos_hist = text.index(MARK_HIST)

    if MARK_COMIS in text:
        pos_com = text.index(MARK_COMIS)
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
    """Yandex card payment."""
    pos_target = text.index(MARK_TARGET)
    pos_date = text.index(MARK_DATE)
    pos_sum = text.index(MARK_TRANS_SUM)
    pos_com = text.index(MARK_COMIS)
    pos_hist = text.index(MARK_HIST)

    return [
      subj, '',
      text[pos_target:pos_date],
      text[pos_date:pos_sum],
      text[pos_sum:pos_com],
      text[pos_com:pos_hist],
    ]


def e_transf_out(subj, text):
    """Transfer out."""
    pos_trans = text.index('Назначение платежа')
    pos_date = text.index(MARK_DATE)
    pos_sum = text.index('Со счета списано')
    pos_avail = text.index(MARK_AVAIL)
    pos_hist = text.index(MARK_HIST)

    return [
      subj, '',
      text[pos_trans:pos_date],
      text[pos_date:pos_sum],
      text[pos_sum:pos_avail],
      text[pos_avail:pos_hist],
    ]


def e_week(subj, text):
    """Week note."""
    pos1 = text.index('баланс на ')
    pos2 = text.index('Где получать баллы')

    return [
      subj, '',
      text[pos1:pos2],
    ]


def e_transf_in(subj, text):
    """Transfer income."""
    pos_date = text.index(MARK_DATE)
    pos_sum = text.index(MARK_TRANS_SUM)
    pos_avail = text.index(MARK_AVAIL)
    pos_hist = text.index(MARK_HIST)
    comment = 'Комментарий'

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
    """Income1."""
    pos_date = text.index(MARK_DATE)
    pos_trans = text.index(MARK_TRANS_IN)
    pos_sum = text.index(MARK_TRANS_SUM)
    pos_avail = text.index(MARK_AVAIL)
    pos_hist = text.index('Все детали пополнения')

    return [
      subj, '',
      text[pos_date:pos_trans], text[pos_trans:pos_sum],
      text[pos_sum:pos_avail], text[pos_avail:pos_hist],
    ]


def e_income(subj, text):
    """Income."""
    pos_date = text.index(MARK_DATE)
    pos_trans = text.index(MARK_TRANS_IN)
    pos_sum = text.index(MARK_TRANS_SUM)
    pos_avail = text.index(MARK_AVAIL)
    pos_hist = text.index(MARK_HIST)

    return [
      subj, '',
      text[pos_date:pos_trans],
      text[pos_trans:pos_sum],
      text[pos_sum:pos_avail],
      text[pos_avail:pos_hist],
    ]


def e_cashback(subj, _text):
    """Cashback."""
    return [
      'Напоминание о кэшбэк', '', subj,
    ]


def e_cash(subj, text):
    """Cash out."""
    pos_card = text.index(MARK_CARD)
    pos_bank = text.index('Банкомат')
    pos_date = text.index(MARK_DATE)
    pos_cash = text.index('Выданная сумма')
    pos_comis = text.index('Комиссия за снятие')
    pos_curr = text.index('Сумма в валюте операции')
    pos_place = text.index(MARK_PLACE)
    pos_avail = text.index(MARK_AVAIL)
    pos_limit = text.index('В этом месяце вы можете снять')
    pos_hist = text.index('Запись обо всех операциях')

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
    """Payment."""
    pos_card = text.index(MARK_CARD)
    pos_target = text.index(MARK_TARGET)
    pos_date = text.index(MARK_DATE)
    pos_summ = text.index('Сколько списано')
    pos_place = text.index(MARK_PLACE)
    pos_avail = text.index(MARK_AVAIL)
    pos_hist = text.index('Запись о платеже хранится')

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
SUBJ_ONLY = [
  ('Информация о платеже',),
  ('Статус распоряжения:',),
  ('Как насчёт вашей подписки',),
  ('Получайте ', 'годовых'),
  ('Переводы с комиссией',),
  ('сундук с призами',),
  ('На всякий случай:',),
  ('Несколько вопросов',),
  ('Получите подарок',),
  ('Выиграйте',),
  ('Повышенный кэшбэк',),
  ('Получайте кэшбэк',),
  ('Списание средств',),
  ('поступили денежные средства',),
  ('о важном',),
  ('найдёт для вас кэшбэк',),
  ('Сохраните свои деньги',),
  ('Вход', 'от имени клиента'),
  ('Транзакция по банковской карте',),
  ('Автоплатежи',),
  ('Получите бонус',),
  ('Поступление зарплаты',),
  ('Инвестируйте',),
  ('возврат по операции',),
]


def start(subj, body):
    """Parse Yandex Money."""
    title = 'ЮMoney: '
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

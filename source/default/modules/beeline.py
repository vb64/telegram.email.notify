"""Beeline.ru."""
from html2text import convert
from . import by_subj, NBSP, BUTTONS

MARK_INBOX = 'В Ваш почтовый ящик '
MARK_CLOUD_GO = 'Прослушать сообщение можно в web-интерфейсе управления услугой'


def voice_mail(_subj, text):
    """Voice mail."""
    pos_start = text.index(MARK_INBOX)
    pos_end = text.index(MARK_CLOUD_GO)
    result = text[pos_start:pos_end]

    if 'отабонента' in result:
        result = result.replace('отабонента', 'от абонента')

    return [
      result,
      '\n' + BUTTONS + '\n' + "[Прослушать](https://cloudpbx.beeline.ru/)",
    ]


SUBJ_HANDLERS = [
  (('Облачная АТС - У вас новое сообщение голосовой почты', ), voice_mail),
]


def start(subj, body):
    """Parse Beeline."""
    return by_subj(
      subj,
      body,
      convert(body).replace(NBSP, ' '),
      'beeline',
      'Beeline Облачная АТС\n',
      SUBJ_HANDLERS
    )

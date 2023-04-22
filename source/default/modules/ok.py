"""Odnoklassniki.ru."""
from html2text import convert
from models import SavedSource
from modutil import is_present, by_subj, BUTTONS, NBSP

LABEL = 'ok'

SUBJ_POST = 'Пока вас не было'
SUBJ_PRESENT = 'вам подарок'

BUTT_VIWEW = "[Посмотреть]({})"

MARK_PHOTO = [' добавил', ' фото']
MARK_PHOTO_REF = '.PHOTO_ADDED'

MARK_NOTE = [' создал', ' заметку']
MARK_NOTE_REF = '.USER_MEDIA_TOPIC_NEW_CREATED'

MARK_PROFILE_REF = 'https://ok.ru/profile/'


def make_link(txt, ref, note):
    """Button with link."""
    actor = note
    if MARK_PROFILE_REF in txt:
        actor = txt[:txt.index(MARK_PROFILE_REF)]
        actor = actor[actor.rindex(SUBJ_POST) + len(SUBJ_POST):].strip() + ' ' + note

    link = ''
    for word in txt.split():
        if is_present([MARK_PROFILE_REF, ref], word):
            link = BUTT_VIWEW.format(word[word.index(MARK_PROFILE_REF):])
            break

    return [actor, '', BUTTONS, link]


def e_message(subj, text):
    """Message."""
    txt = convert(text, extract_link=True).replace(NBSP, ' ')
    ret = [txt]

    if is_present(MARK_PHOTO + [MARK_PHOTO_REF], txt):
        ret = make_link(txt, MARK_PHOTO_REF, 'новое фото')
    elif is_present(MARK_NOTE + [MARK_NOTE_REF], txt):
        ret = make_link(txt, MARK_NOTE_REF, 'новая заметка')
    else:
        SavedSource(label='ok_text', subject=subj, body=text).put()

    return ret


def e_present(subj, text):
    """Present."""
    link = ""
    lines = iter(text.splitlines())
    for line in lines:
        if is_present(['https://ok.ru/?', 'lookPresent'], line):
            link = BUTT_VIWEW.format(line)
            break

    return [subj, '', BUTTONS, link]


SUBJ_HANDLERS = [
  ((SUBJ_POST, ), e_message),
  ((SUBJ_PRESENT, ), e_present),
]


def start(subj, body):
    """Parse Odnoklassniki.ru."""
    return by_subj(subj, body, body, LABEL, 'Одноклассники: ', SUBJ_HANDLERS)

"""Util for modules."""
from html2text import convert
from models import SavedSource

MARKUP = '###text_mode markdown'
BUTTONS = '###buttons'
NBSP = chr(0xC2) + chr(0xA0)


def store(label, subj, body):
    """Default handler for store incoming messages."""
    SavedSource(label=label, subject=subj, body=body).put()
    return subj + '\n' + convert(body, extract_link=True).replace(NBSP, ' ')


def is_present(marks, text):
    """Return True, if all marks present in given text."""
    return all([mark in text for mark in marks])  # pylint: disable=use-a-generator


def by_subj(subj, body, text, label, prefix, handlers):  # pylint: disable=too-many-arguments
    """Process message by subject."""
    for marks, func in handlers:
        if is_present(marks, subj):
            return prefix + '\n'.join(func(subj, text))

    # unknown subject, save to db for analizing and return default answer
    SavedSource(label=label, subject=subj, body=body).put()

    return prefix + subj + '\n' + text


def is_href(text):
    """Text looks like href."""
    return any([
      text.startswith('https://'),
      text.startswith('http://'),
    ])


def add_href(words, text):
    """Save text as markdown link."""
    if not words:
        add_word(words, text)
        return

    last_word = words[-1]
    if last_word[1]:  # already link
        add_word(words, text)
        return

    words[-1] = ("[{}]({})".format(last_word[0], text), True)


def clear_markdown(text):
    """Clear special markdown symbols from text."""
    for i in ['*', '_', '`', '’']:
        text = text.replace(i, '')

    return text


def add_word(words, text):
    """Save simple text."""
    words.append((clear_markdown(text), False))


def make_markdown(text):
    """Embed url as markdown links."""
    result = []
    for word in text.split():
        if is_href(word):
            add_href(result, word)
        else:
            add_word(result, word)

    return ' '.join([i[0] for i in result])

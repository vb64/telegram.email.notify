"""
modules for transform
"""
from models import SavedSource

MARKUP = '### text_mode markdown'
BUTTONS = '### buttons'
NBSP = chr(0xC2) + chr(0xA0)


def by_subj(subj, body, text, label, prefix, handlers):  # pylint: disable=too-many-arguments
    """
    process message by subject
    """
    for marks, func in handlers:
        if all([mark in subj for mark in marks]):
            return prefix + '\n'.join(func(subj, text))

    # unknown subject, save to db for analizing and return default answer
    SavedSource(label=label, subject=subj, body=body).put()

    return prefix + subj + '\n' + text

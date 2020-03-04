"""
Twitter
"""
from . import by_subj

LABEL = 'twitter'
SUBJ_HIGHLIGHTS = 'Your Highlights'
MARK_MORE = 'Read more at Twitter'


def e_post(subj, text):
    """
    'Your Highlights'
    """
    return [subj, '', text[:text.index(MARK_MORE)]]


SUBJ_HANDLERS = [
  ((SUBJ_HIGHLIGHTS, ), e_post),
]


def start(_subj, body):
    """
    parse Twitter message
    """
    lines = body.splitlines()
    return by_subj(lines[0], body, '\n'.join(lines[1:]), LABEL, 'Twitter: ', SUBJ_HANDLERS)

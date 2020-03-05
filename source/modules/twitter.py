"""
Twitter
"""
from models import SavedSource
from . import by_subj

LABEL = 'twitter'
SUBJ_HIGHLIGHTS = "Your Highlights"
SUBJ_HAPPENING = "What's happening"

MARK_MORE = 'Read more at Twitter'


def e_post(subj, text):
    """
    'Your Highlights'
    """
    return [subj, '', text[:text.index(MARK_MORE)]]


SUBJ_HANDLERS = [
  ((SUBJ_HIGHLIGHTS, ), e_post),
  ((SUBJ_HAPPENING, ), e_post),
]


def start(subj, body):
    """
    parse Twitter message
    """
    SavedSource(label=LABEL, subject=subj, body=body).put()

    lines = body.splitlines()
    text = '\n'.join(lines[1:])

    return by_subj(lines[0], text, text, 'twitter_text', 'Twitter: ', SUBJ_HANDLERS)

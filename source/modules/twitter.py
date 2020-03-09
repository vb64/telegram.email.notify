"""
Twitter
"""
from models import SavedSource

LABEL = 'twitter'
TITLE = 'Twitter: '

SUBJECTS = [
  "Your Highlights",
  "What's happening",
]

TERMINALS = [
  "Read more at Twitter",
  "Go to Moment",
]


def cut_text(text):
    """
    extract and return news text
    """
    for phrase in TERMINALS:
        if phrase in text:
            return text[:text.index(phrase)]

    SavedSource(label=LABEL, subject='cut_text', body=text).put()
    return text


def start(subj, body):
    """
    parse Twitter message
    """
    lines = body.splitlines()
    for index, line in enumerate(lines):
        if line in SUBJECTS:
            text = '\n'.join(lines[index + 1:])
            return TITLE + line + '\n' + cut_text(text)

    SavedSource(label=LABEL, subject=subj, body=body).put()

    return TITLE + subj

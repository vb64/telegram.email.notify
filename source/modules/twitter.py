"""
Twitter
"""
from models import SavedSource

LABEL = 'twitter'

SUBJECTS = [
  "Your Highlights",
  "What's happening",
]


def start(subj, body):
    """
    parse Twitter message
    """
    lines = body.splitlines()
    for index, line in enumerate(lines):
        if line in SUBJECTS:
            text = '\n'.join(lines[index + 1:])
            return 'Twitter: ' + line + '\n' + text[:text.index('Read more at Twitter')]

    SavedSource(label=LABEL, subject=subj, body=body).put()

    return 'Twitter: ' + subj

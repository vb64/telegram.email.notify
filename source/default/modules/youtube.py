"""YouTube stuff."""
from models import SavedSource
from . import by_subj, MARKUP

LABEL = 'youtube'
POST_URL = 'http://www.youtube.com/watch?'

SUBJ_LIVE = ' is live now: '
SUBJ_UPLOAD = ' just uploaded a video'


def e_live(subj, text):
    """Check 'is live now:' in subject."""
    blogger, title = subj.split(SUBJ_LIVE)
    url = ''
    link = title

    for line in text.splitlines():
        if line.startswith(POST_URL):
            url = line
            break

    if url:
        link = "[{}]({})".format(title, url)
    else:
        SavedSource(label=LABEL, subject=subj, body=text).put()

    return [blogger, '', MARKUP, link]


def e_upload(subj, text):
    """Check 'just uploaded a video' in subject."""
    blogger, _tmp = subj.split(SUBJ_UPLOAD)
    url = ''
    messages = []

    for line in text.splitlines():
        if line.startswith(POST_URL):
            url = line
            break
        messages.append(line)

    if url:
        blogger = "[{}]({})".format(blogger, url)
    else:
        SavedSource(label=LABEL, subject=subj, body=text).put()

    return [blogger, '', MARKUP, ' '.join(messages)]


SUBJ_HANDLERS = [
  ((SUBJ_LIVE, ), e_live),
  ((SUBJ_UPLOAD, ), e_upload),
]


def start(subj, body):
    """Parse YouTube."""
    return by_subj(subj, body, body, LABEL, 'YouTube: ', SUBJ_HANDLERS)

"""Twitter."""
from models import SavedSource

LABEL = 'twitter'
TITLE = 'Twitter: '

SUBJECTS = [
  "Your Highlights",
  "What's happening",
]
DELIMETER = '  Opt-out: https://twitter.com/'
TERMINALS = [
  "Read more at Twitter",
  "Go to Moment",
]


def cut_text(text):
    """Extract and return news text."""
    for phrase in TERMINALS:
        if phrase in text:
            return text[:text.index(phrase)]

    SavedSource(label=LABEL, subject='cut_text', body=text).put()
    return text


def convert_plain(text):
    """Part text/plain."""
    lines = text.split('\n')
    title = lines[0]
    result = []
    for line in lines[1:]:
        result.append(line.strip())

    return '\n'.join((
      title, '',
      '\n'.join(result)
    ))


def start(subj, body):
    """Parse Twitter message."""
    lines = body.splitlines()
    for index, line in enumerate(lines):
        if line in SUBJECTS:
            text = '\n'.join(lines[index + 1:])
            return TITLE + line + '\n' + cut_text(text)

    if DELIMETER in body:
        return convert_plain(body[:body.index(DELIMETER)])

    SavedSource(label=LABEL, subject=subj, body=body).put()
    return TITLE + subj

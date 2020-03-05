"""
LiveJournal
"""
from models import SavedSource
LABEL = 'lj'


def start(subj, body):
    """
    parse LiveJournal message
    """
    SavedSource(label=LABEL, subject=subj, body=body).put()

    return 'LiveJournal: ' + subj

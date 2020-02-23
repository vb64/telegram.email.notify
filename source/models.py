"""
db model
"""
from google.appengine.ext import ndb


class SavedSource(ndb.Model):  # pylint: disable=too-few-public-methods
    """
    source of inbound requests
    """
    label = ndb.StringProperty(default='')
    subject = ndb.TextProperty(default='')
    body = ndb.TextProperty(default='')

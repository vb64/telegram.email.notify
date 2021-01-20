"""
db model
"""
from google.appengine.ext import ndb
from google.appengine.api import mail


class SavedSource(ndb.Model):  # pylint: disable=too-few-public-methods
    """
    source of inbound requests
    """
    made = ndb.DateTimeProperty(auto_now_add=True)
    label = ndb.StringProperty(default='')
    subject = ndb.TextProperty(default='')
    body = ndb.TextProperty(default='')


class EmailData(ndb.Model):  # pylint: disable=too-few-public-methods
    """
    email origin file data
    """
    made = ndb.DateTimeProperty(auto_now_add=True)
    sent = ndb.DateTimeProperty(indexed=False)
    field_from = ndb.TextProperty(default='')
    field_to = ndb.TextProperty(default='')
    field_subj = ndb.TextProperty(default='')
    field_text = ndb.TextProperty(default='')
    field_html = ndb.TextProperty(default='')

    @classmethod
    def from_upload(cls, reader):
        """
        create from blobstore.BlobReader
        """
        message = mail.InboundEmailMessage(reader.read())

        item = cls()

        item.field_from = message.sender
        item.field_to = message.to
        item.field_subj = message.subject
        # item.field_text
        # item.field_html

        item.put()
        return item

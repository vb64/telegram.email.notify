"""Ndb model."""
from google.appengine.ext import ndb
from google.appengine.api import mail


class SavedSource(ndb.Model):
    """Source of inbound requests."""
    made = ndb.DateTimeProperty(auto_now_add=True)
    label = ndb.StringProperty(default='')
    subject = ndb.TextProperty(default='')
    body = ndb.TextProperty(default='')


class EmailData(ndb.Model):
    """Email origin file data."""
    made = ndb.DateTimeProperty(auto_now_add=True)
    field_from = ndb.TextProperty(default='')
    field_to = ndb.TextProperty(default='')
    field_subj = ndb.TextProperty(default='')
    field_text = ndb.TextProperty(default='')
    field_html = ndb.TextProperty(default='')

    @classmethod
    def from_upload(cls, reader):
        """Create from blobstore.BlobReader."""
        message = mail.InboundEmailMessage(reader.read())

        item = cls()
        try:
            item.field_from = message.sender
            item.field_to = message.to
            item.field_subj = message.subject
            item.field_text = "".join([body.decode() for _ct, body in message.bodies('text/plain')])
            item.field_html = "".join([body.decode() for _ct, body in message.bodies('text/html')])
        except AttributeError:
            raise

        item.put()
        return item

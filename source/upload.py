"""
File upload handlers
"""
from google.appengine.ext import webapp, blobstore
from google.appengine.ext.webapp import blobstore_handlers
from models import EmailData


class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    """
    GAE upload handler class
    """
    def post(self):  # pylint: disable=arguments-differ
        """
        POST handler
        """
        bodies = self.get_uploads('emailbody')
        if len(bodies) < 1:
            return self.redirect('/email/')

        edata = EmailData.from_upload(blobstore.BlobReader(bodies[0]))
        bodies[0].delete()

        return self.redirect('/email/{}/'.format(edata.key().id))


APP = webapp.WSGIApplication([('/upload/', UploadHandler)], debug=True)

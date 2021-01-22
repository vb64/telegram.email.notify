"""
make test T=test_upload.py
"""
from . import TestCase


class MockBody:  # pylint: disable=too-few-public-methods
    """
    mock UploadHandler.get_uploads return item
    """
    def __init__(self, file_name):
        self.file_name = file_name

    def delete(self):
        """
        emulate file deletion
        """
        self.file_name = None


class MockReader:  # pylint: disable=too-few-public-methods
    """
    mock blobstore.BlobReader
    """
    def __init__(self, body):
        self.body = body

    def read(self):
        """
        return content of given file
        """
        return open(self.body.file_name, 'rb').read()


class TestUpload(TestCase):
    """
    upload .eml file
    """
    def setUp(self):
        TestCase.setUp(self)

        from google.appengine.ext import blobstore
        from upload import UploadHandler

        class MockHandler(UploadHandler):
            """
            mock webapp.WSGIApplication upload handler
            """
            def __init__(self, mock_bodies):  # pylint: disable=super-init-not-called
                self.mock_bodies = [MockBody(i) for i in mock_bodies]

            def get_uploads(self, _field_name):  # pylint: disable=signature-differs
                """
                mock uploaded file list
                """
                return self.mock_bodies

            def redirect(self, url):  # pylint: disable=arguments-differ
                """
                mock uploaded file list
                """
                return url

        self.save_blob = blobstore.BlobReader
        blobstore.BlobReader = MockReader
        self.mock_handler = MockHandler

    def tearDown(self):
        from google.appengine.ext import blobstore

        blobstore.BlobReader = self.save_blob
        TestCase.tearDown(self)

    def test_email_upload(self):
        """
        email upload page
        """
        handler = self.mock_handler([])
        assert handler.post() == '/'

        handler = self.mock_handler([self.get_fixture_path('reddit01.eml')])
        assert '/email/' in handler.post()

        handler = self.mock_handler([self.get_fixture_path('msg01.html')])
        assert handler.post() == '/'

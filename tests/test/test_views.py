"""App views.

make test T=test_views.py
"""
from flask import escape
from . import TestCase


class TestCaseViews(TestCase):
    """Site views."""

    codec = 'ym'
    src = 'subject\ntest text'

    def test_mainpage(self):
        """Root page."""
        response = self.simple_view('mainpage')
        assert response.status_code == 200
        assert '/upload/' in response.data

    def test_transform(self):
        """Transform page."""
        assert self.param_view('transform', {'codec': 'xxx'}, return_code=405).status_code == 405
        assert self.param_post('transform', {'codec': 'xxx'}, {}).status_code == 404

        response = self.param_post('transform', {'codec': self.codec}, self.src)

        assert response.status_code == 200
        assert self.src in response.data

    def test_store(self):
        """Store func."""
        response = self.param_post('transform', {'codec': 'store'}, self.src)
        assert response.status_code == 200
        assert self.src in response.data

    def test_run(self):
        """Run function with exception raise."""
        from main import run
        import modules

        def mock_store(label, subj, body):
            """Emulate exception raise."""
            raise Exception(''.join([label, subj, body]))  # pylint: disable=broad-exception-raised

        saved = modules.store
        modules.store = mock_store

        with self.assertRaises(Exception) as context:
            run('store', 'xxx')
        assert 'xxx' in str(context.exception)

        modules.store = saved

    def test_testdata(self):
        """Run function with testdata."""
        response = self.param_post('transform', {'codec': 'store'}, 'testdata')
        assert response.status_code == 200
        assert response.data == 'OK'

    def test_email(self):
        """Email page."""
        response = self.guest_view('/email/666/', return_code=404)
        assert response.status_code == 404

        from models import EmailData

        item = EmailData()
        item.field_from = "xxxx"
        item.field_to = "zzz"
        item.field_subj = "yyy"
        item.field_text = "123 456"
        item.field_html = "<html></html>"
        item.put()

        response = self.guest_view('/email/{}/'.format(item.key.id()))
        assert response.status_code == 200

        assert item.field_from in response.data
        assert item.field_to in response.data
        assert item.field_subj in response.data
        assert item.field_text in response.data
        assert escape(item.field_html) in response.data

        response = self.client.post(
          '/email/{}/'.format(item.key.id()),
          data={'codec': self.codec},
          follow_redirects=True
        )
        assert response.status_code == 200

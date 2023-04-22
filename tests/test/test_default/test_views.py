"""App views.

make test T=test_default/test_views.py
"""
import io
from flask import escape
from . import TestDefault


class TestViews(TestDefault):
    """Site views."""

    codec = 'ym'
    src = 'subject\ntest text'

    def test_mainpage(self):
        """Root page."""
        response = self.simple_view('mainpage')
        assert response.status_code == 200
        assert '/upload/' in response.get_data(as_text=True)

    def test_upload(self):
        """Eml upload."""
        from models import EmailData

        self.check_db_tables([(EmailData, 0)])

        response = self.simple_post('upload', {})
        assert response.status_code == 200
        assert 'Select .eml file for upload' in response.get_data(as_text=True)

        response = self.simple_post('upload', {'emailbody': (io.BytesIO(b'xxx'), "wrong.eml")})
        assert response.status_code == 200
        assert 'Select .eml file for upload' in response.get_data(as_text=True)

        self.check_db_tables([(EmailData, 0)])

        response = self.simple_post(
          'upload',
          {'emailbody': (open(self.get_fixture_path('reddit01.eml'), 'rb'), "reddit.eml")}
        )
        assert response.status_code == 200
        text = response.get_data(as_text=True)
        assert 'Select .eml file for upload' not in text
        assert 'Email visualization' in text
        self.check_db_tables([(EmailData, 1)])

    def test_transform(self):
        """Transform page."""
        assert self.param_view('transform', {'codec': 'xxx'}, return_code=405).status_code == 405
        assert self.param_post('transform', {'codec': 'xxx'}, {}).status_code == 404

        response = self.param_post('transform', {'codec': self.codec}, self.src)

        assert response.status_code == 200
        assert self.src in response.get_data(as_text=True)

    def test_store(self):
        """Store func."""
        response = self.param_post('transform', {'codec': 'store'}, self.src)
        assert response.status_code == 200
        assert self.src in response.get_data(as_text=True)

    def test_run(self):
        """Run function with exception raise."""
        from main import run
        import modutil

        def mock_store(label, subj, body):
            """Emulate exception raise."""
            raise Exception(''.join([label, subj, body]))  # pylint: disable=broad-exception-raised

        saved = modutil.store
        modutil.store = mock_store

        with self.assertRaises(Exception) as context:
            run('store', 'xxx')
        assert 'xxx' in str(context.exception)

        modutil.store = saved

    def test_testdata(self):
        """Run function with testdata."""
        response = self.param_post('transform', {'codec': 'store'}, 'testdata')
        assert response.status_code == 200
        assert response.get_data(as_text=True) == 'OK'

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
        text = response.get_data(as_text=True)

        assert item.field_from in text
        assert item.field_to in text
        assert item.field_subj in text
        assert item.field_text in text
        assert escape(item.field_html) in text

        response = self.client.post(
          '/email/{}/'.format(item.key.id()),
          data={'codec': self.codec},
          follow_redirects=True
        )
        assert response.status_code == 200

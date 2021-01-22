"""
make test T=test_models.py
"""
from . import TestCase


class TestModels(TestCase):
    """
    models.py
    """
    def test_from_upload(self):
        """
        EmailData.from_upload
        """
        from models import EmailData

        edata = EmailData.from_upload(open(self.get_fixture_path('reddit01.eml')))

        assert 'noreply@redditmail.com' in edata.field_from
        assert 'vit.sar68@gmail.com' in edata.field_to
        assert 'What was the worst pet name' in edata.field_subj
        # assert edata.field_text == 'xxx'
        # assert edata.field_html == 'xxx'

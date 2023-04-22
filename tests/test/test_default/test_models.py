"""Ndb models.

make test T=test_default/test_models.py
"""
from . import TestDefault


class TestModels(TestDefault):
    """Module models."""

    def test_from_upload(self):
        """Check EmailData.from_upload."""
        from models import EmailData

        edata = EmailData.from_upload(open(self.get_fixture_path('reddit01.eml'), encoding='utf-8'))

        assert 'noreply@redditmail.com' in edata.field_from
        assert 'vit.sar68@gmail.com' in edata.field_to
        assert 'What was the worst pet name' in edata.field_subj

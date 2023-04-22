"""Backup app endpoints.

make test T=test_backend/test_back.py
"""
from datetime import datetime, timedelta
from . import TestBackend


class TestBack(TestBackend):
    """Backup web endpoints."""

    def test_empty(self):
        """No records."""
        from back import main
        assert 'deleted: 0' in main()

    def test_filled(self):
        """Filled table case."""
        import back
        from back import SavedSource

        save1 = back.PORTION
        save2 = back.PARTS

        back.PORTION = 3
        back.PARTS = 1
        date = datetime.utcnow() - timedelta(days=back.DAYS_OLD + 1)

        for _i in range(5):
            record = SavedSource()
            record.made = date
            record.put()

        assert back.purge_model(SavedSource, datetime.utcnow() - timedelta(days=back.DAYS_OLD)) == 3

        back.PORTION = save1
        back.PARTS = save2

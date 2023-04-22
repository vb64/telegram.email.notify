"""Backup app endpoints.

make test T=test_backend/test_back.py
"""
# from datetime import datetime, timedelta
from . import TestBackend


class TestBack(TestBackend):
    """Backup web endpoints."""

    def test_empty(self):
        """No records."""
        from back import main
        assert 'deleted: 0' in main()

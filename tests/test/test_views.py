"""
make test T=test_views.py
"""
from . import TestCase


class TestCaseViews(TestCase):
    """
    site views
    """
    def test_warmup(self):
        """
        /_ah/warmup
        """
        assert self.simple_view('warmup').status_code == 200

    def test_backend_start(self):
        """
        /_ah/start
        """
        assert self.simple_view('backend_start').status_code == 200

    def test_mainpage(self):
        """
        root page
        """
        assert self.simple_view('mainpage').status_code == 200

    def test_transform(self):
        """
        root page post
        """
        src = 'test text'
        response = self.simple_post('transform', {'codecs': 'ym', 'source': src})
        assert response.status_code == 200
        assert src in response.data

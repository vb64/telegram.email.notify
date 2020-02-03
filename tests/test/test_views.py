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

        src = 'test text'
        response = self.simple_post('mainpage', {'codec': 'ym', 'source': src})
        assert response.status_code == 200
        assert src in response.data

    def test_transform(self):
        """
        transform page
        """
        assert self.param_view('transform', {'codec': 'xxx'}, return_code=405).status_code == 405
        assert self.param_post('transform', {'codec': 'xxx'}, {}).status_code == 404

        src = 'test text'
        codec = 'ym'

        response = self.param_post('transform', {'codec': codec}, src)

        assert response.status_code == 200
        assert src in response.data

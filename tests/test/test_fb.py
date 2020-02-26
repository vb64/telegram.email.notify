"""
make test T=test_fb.py
"""
from . import TestCase


class TestFB(TestCase):
    """
    FaceBook
    """
    def transfer(self, fname):
        """
        transfer fixture by facebook
        """
        from modules.fb import start
        return self.start_transfer(fname, start, 'fb')

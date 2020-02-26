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

    def test_comment(self):
        """
        comment
        """
        mark = "https://www.facebook.com/email_forward_notice"

        text = self.transfer('comment.txt')
        assert mark not in text

    def test_broken_comment(self):
        """
        broken comment
        """
        mark = "https://www.facebook.com/email_forward_notice"

        text = self.transfer('comment1.txt')
        assert mark not in text

        text = self.transfer('comment2.txt')
        assert mark in text

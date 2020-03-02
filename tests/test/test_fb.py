"""
make test T=test_fb.py
"""
from . import TestCase


class TestFB(TestCase):
    """
    FaceBook
    """
    mark = "https://www.facebook.com/email_forward_notice"

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
        text = self.transfer('comment.txt')
        assert self.mark not in text

    def test_broken_comment(self):
        """
        broken comment
        """
        text = self.transfer('comment1.txt')
        assert self.mark not in text

        text = self.transfer('comment2.txt')
        assert self.mark in text

    def test_photo(self):
        """
        photo
        """
        text = self.transfer('photo.txt')
        assert self.mark not in text

        text = self.transfer('photo1.txt')
        assert self.mark not in text

        text = self.transfer('update.txt')
        assert self.mark not in text

    def test_recomendation(self):
        """
        recomendation
        """
        text = self.transfer('recomendation.txt')
        assert self.mark not in text

    def test_friend(self):
        """
        friend
        """
        text = self.transfer('friend.txt')
        assert self.mark not in text

        text = self.transfer('friend1.txt')
        assert self.mark not in text

        text = self.transfer('friend2.txt')
        assert self.mark not in text

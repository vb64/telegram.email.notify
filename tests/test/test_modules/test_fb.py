"""FaceBook.

make test T=test_modules/test_fb.py
"""
from . import TestModule


class TestFb(TestModule):
    """FaceBook."""

    def transfer(self, fname):
        """Transfer fixture by facebook."""
        from modules.fb import start
        return self.start_transfer(fname, start, 'fb')

    @staticmethod
    def test_extract_text():
        """Check extract_text."""
        from modules.fb import extract_text
        assert extract_text('') == ''

    @staticmethod
    def test_extract_link():
        """Check extract_link."""
        from modules.fb import extract_link
        assert extract_link('xxx') == ''

    def test_poll(self):
        """Check poll."""
        text = self.transfer('poll.txt')
        assert 'https://www.facebook.com/nd/?' in text
        assert "создал опрос" in text

    def test_publication(self):
        """Check publication."""
        text = self.transfer('publication.txt')
        assert 'https://www.facebook.com/nd/?' in text
        assert "сделал публикацию" in text

    def test_video(self):
        """Check video."""
        text = self.transfer('video.txt')
        assert 'https://www.facebook.com/nd/?' in text
        assert "опубликовал видео" in text

# -*- coding: utf-8 -*-
"""
make test T=test_fb.py
"""
from . import TestCase


class TestFb(TestCase):
    """
    FaceBook
    """
    def transfer(self, fname):
        """
        transfer fixture by facebook
        """
        from modules.fb import start
        return self.start_transfer(fname, start, 'fb')

    @staticmethod
    def test_extract_text():
        """
        extract_text
        """
        from modules.fb import extract_text
        assert extract_text('') == ''

    @staticmethod
    def test_extract_link():
        """
        extract_link
        """
        from modules.fb import extract_link
        assert extract_link('xxx') == ''

    def test_poll(self):
        """
        poll
        """
        text = self.transfer('poll.txt')
        assert 'https://www.facebook.com/nd/?' in text
        assert u"создал опрос" in text

    def test_publication(self):
        """
        publication
        """
        text = self.transfer('publication.txt')
        assert 'https://www.facebook.com/nd/?' in text
        assert u"сделал публикацию" in text

    def test_video(self):
        """
        video
        """
        text = self.transfer('video.txt')
        assert 'https://www.facebook.com/nd/?' in text
        assert u"опубликовал видео" in text
        # print text.encode('cp866', 'ignore')

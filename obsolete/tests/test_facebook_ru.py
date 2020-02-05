"""
make test T=test_modules.test_facebook_ru
"""
from modules import facebook_ru
from . import TestCaseModule


class TestFacebookRu(TestCaseModule):

    def test_wrong(self):
        source = "Test text"
        self.assertEqual(facebook_ru.start(source), source)

    def test_dflt(self):
        from fixtures.facebook_ru import source, result
        self.assertEqual(facebook_ru.start(source), result)

# python tests.py ../source test.test_modules.test_forex
from modules import forex
from . import TestCaseModule


class TestCaseForex(TestCaseModule):

    def test_wrong(self):
        source = "Test text"
        self.assertEqual(forex.start(source), source)

    def test_dflt(self):
        from fixtures.forex import source, result, broken, source1, result1
        self.assertEqual(forex.start(source), result)
        self.assertEqual(forex.start(broken), broken)
        self.assertEqual(forex.start(source1), result1)

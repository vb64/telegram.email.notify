# python tests.py ../source test.test_modules.test_rybaodessa_fb
from modules import rybaodessa_fb
from . import TestCaseModule


class TestCaseRybaodessaFb(TestCaseModule):

    def test_wrong(self):
        source = "Test text"
        self.assertEqual(rybaodessa_fb.start(source), source)

    def test_dflt(self):
        from fixtures.rybaodessa_fb import source, result, broken
        self.assertEqual(rybaodessa_fb.start(source), result)
        self.assertEqual(rybaodessa_fb.start(broken), broken)

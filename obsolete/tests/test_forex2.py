# python tests.py ../source test.test_modules.test_forex2
from modules import forex2
from . import TestCaseModule


class TestCaseForex2(TestCaseModule):

    def test_wrong(self):
        source = "Test text"
        self.assertEqual(forex2.start(source), source)

    def test_dflt(self):
        from fixtures.forex2 import source, result, broken1, broken2
        self.assertEqual(forex2.start(source), result)
        self.assertEqual(forex2.start(broken1), broken1)
        self.assertEqual(forex2.start(broken2), broken2)

        from fixtures.forex2 import source1, result1, source2, result2, source3, result3, source4, result4
        self.assertEqual(forex2.start(source1), result1)
        self.assertEqual(forex2.start(source2), result2)
        self.assertEqual(forex2.start(source3), result3)
        self.assertEqual(forex2.start(source4), result4)

        from fixtures.forex2 import broken3, broken4, broken5, broken6, broken7
        self.assertEqual(forex2.start(broken3), broken3)
        self.assertEqual(forex2.start(broken4), broken4)
        self.assertEqual(forex2.start(broken5), broken5)
        self.assertEqual(forex2.start(broken6), broken6)
        self.assertEqual(forex2.start(broken7), broken7)

# python tests.py ../source test.test_modules.test_rybaodessa_forum
from modules import rybaodessa_forum
from . import TestCaseModule


class TestCaseRybaodessaForum(TestCaseModule):

    def test_wrong(self):
        source = "Test text"
        self.assertEqual(rybaodessa_forum.start(source), source)

    def test_dflt(self):
        from fixtures.rybaodessa_forum import source1, result1, source2, result2, source3, result3
        self.assertEqual(rybaodessa_forum.start(source1), result1)
        self.assertEqual(rybaodessa_forum.start(source2), result2)
        self.assertEqual(rybaodessa_forum.start(source3), result3)

        from fixtures.rybaodessa_forum import source5, result5
        self.assertEqual(rybaodessa_forum.start(source5), result5)

        from fixtures.rybaodessa_forum import broken1, broken2, broken3, result4
        self.assertEqual(rybaodessa_forum.start(broken1), broken1)
        self.assertEqual(rybaodessa_forum.start(broken2), broken2)
        self.assertEqual(rybaodessa_forum.start(broken3), result4)

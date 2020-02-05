# python tests.py ../source test.test_modules.test_init
from modules import remove_line_with, remove_new_lines
from . import TestCaseModule


class TestCaseInit(TestCaseModule):

    def test_remove_line_with(self):
        source = "Test text\nLine one\nLine two"
        result = "Test text\nLine two"
        self.assertEqual(remove_line_with(source, " one"), result)

        self.assertEqual(remove_line_with(source, "xxx"), source)
        self.assertEqual(remove_line_with(source, " text"), source)
        self.assertEqual(remove_line_with(source, " two"), source)

    def test_remove_new_lines(self):
        source = "\nTest text\n\n\nLine one\nLine two"
        result = "Test text\n\nLine one\nLine two"
        self.assertEqual(remove_new_lines(source), result)

        source = "Test text\n\nLine one\nLine two"
        self.assertEqual(remove_new_lines(source), source)

"""Modules init.

make test T=test_modules/test_init.py
"""
from . import TestModule


class TestInit(TestModule):
    """Module init."""

    @staticmethod
    def test_add_href():
        """Add_href."""
        from modutil import add_href

        words = []
        add_href(words, 'xxx')
        assert words == [('xxx', False)]

        words = [('xxx', True)]
        add_href(words, 'yyy')
        assert words == [('xxx', True), ('yyy', False)]

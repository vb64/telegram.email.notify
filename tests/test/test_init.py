# -*- coding: utf-8 -*-
"""
make test T=test_init.py
"""
from . import TestCase


class TestInit(TestCase):
    """
    module.init
    """
    @staticmethod
    def test_add_href():
        """
        add_href
        """
        from modules import add_href

        words = []
        add_href(words, 'xxx')
        assert words == [('xxx', False)]

        words = [('xxx', True)]
        add_href(words, 'yyy')
        assert words == [('xxx', True), ('yyy', False)]

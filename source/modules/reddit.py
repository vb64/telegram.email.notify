# -*- coding: utf-8 -*-
"""
Reddit
"""
from html2text2 import Parser
from . import is_present

MARK_POSTED = 'Posted by'


def start(subj, body):
    """
    parse Reddit message
    """
    parser = Parser(True, True)
    parser.feed(body)
    parser.close()
    text = parser.text()
    lines = []

    for line in text.split('\n')[2:]:
        if is_present(('VIEW MORE', 'POSTS '), line):
            break
        lines.append(line)

    return 'Reddit: ' + subj + '\n\n' + '\n'.join(lines)

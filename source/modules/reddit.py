# -*- coding: utf-8 -*-
"""
Reddit
"""
from html2text2 import Parser
from . import is_present, make_markdown


class Section:
    """
    Reddit message section
    """
    def __init__(self):
        self.lines = []
        self.read_more = None
        self.comments = None
        self.votes = None

    def __unicode__(self):
        return u"{}\n\n{} {} {}".format(
          '\n\n'.join(self.lines),
          self.read_more,
          self.comments,
          self.votes,
        )

    def __str__(self):
        return self.__unicode__().encode('utf-8')

    def add_line(self, text):
        """
        return true if detected end if section
        """
        if text.endswith(' Votes '):
            return self.add_votes(text)
        elif text.endswith(' Comments '):
            return self.add_comments(text)
        elif text.startswith('Read ') and text.endswith(' More '):
            return self.add_readmore(text)
        else:
            if text.strip():
                self.lines.append(make_markdown(text.decode('utf-8')))
            return False

    def add_readmore(self, text):
        """
        line with read more link
        """
        words = text.split()
        self.read_more = "Read [more]({})".format(words[1])
        return False

    def add_comments(self, text):
        """
        line with comments
        """
        words = text.split()
        self.comments = "comments [{}]({})".format(words[0], words[1])
        return False

    def add_votes(self, text):
        """
        line with votes
        """
        words = text.split()
        self.votes = "votes [{}]({})".format(words[0], words[1])
        return True


def start(_subj, body):
    """
    parse Reddit message
    """
    parser = Parser(True, True)
    parser.feed(body)
    parser.close()
    text = parser.text()
    sections = []
    section = Section()

    for line in text.split('\n')[2:]:
        if is_present(('VIEW MORE', 'POSTS '), line):
            break
        if section.add_line(line):
            sections.append(str(section))
            section = Section()

    return 'Reddit news' + '\n\n' + '\n\n'.join(sections)

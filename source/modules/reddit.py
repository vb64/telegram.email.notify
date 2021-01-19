"""
Reddit
"""
from html2text2 import Parser
from . import is_href, is_present, MARKUP


def clear_links(text):
    """
    Clear links from text
    """
    words = []
    for i in text.split():
        if not is_href(i):
            words.append(i)

    return ' '.join(words)


class Section:
    """
    Reddit message section
    """
    def __init__(self, text):
        self.skiplines = [
          ' Votes ',
          ' Comments ',
        ]
        self.lines = [clear_links(text)]
        self.read_more = None

    def __unicode__(self):
        return "{}\n\n{}".format(
          '\n\n'.join(self.lines),
          self.read_more,
        )

    def __str__(self):
        return self.__unicode__()

    def add_line(self, text):
        """
        return true if detected end if section
        """
        for i in self.skiplines:
            if text.endswith(i):
                return

        if text.startswith('Read ') and text.endswith(' More '):
            self.add_readmore(text)
        else:
            if text.strip():
                self.lines.append(clear_links(text))

    def add_readmore(self, text):
        """
        line with read more link
        """
        words = text.split()
        self.read_more = "[Read more]({})".format(words[1])
        return False


def start(_subj, body):
    """
    parse Reddit message
    """
    parser = Parser(True, True)
    parser.feed(body)
    parser.close()
    text = parser.text()
    sections = []
    section = None

    for line in text.split('\n')[2:]:
        if 'Posted by ' in line:
            if section:
                sections.append(str(section))
            section = Section(line)
            continue

        if is_present(('VIEW MORE', 'POSTS '), line):
            break

        if section:
            section.add_line(line)

    sections.append(str(section))

    return MARKUP + '\n' 'Reddit news' + '\n\n' + '\n\n'.join(sections)

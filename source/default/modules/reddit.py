"""Reddit."""
from html2text2 import Parser
from . import is_href, is_present, clear_markdown, MARKUP


def clear_links(text):
    """Clear links from text."""
    words = []
    for i in text.split():
        if not is_href(i):
            words.append(i)

    return ' '.join(words)


class Section:
    """Reddit message section."""

    skiplines = [
      ' Votes ',
      ' Comments ',
    ]

    def __init__(self, text):
        """Section with text."""
        self.lines = [clear_links(text)]
        self.read_more = None

    def __str__(self):
        """Text representation."""
        return "{}\n\n{}".format(
          clear_markdown('\n\n'.join(self.lines)),
          self.read_more if self.read_more else '',
        )

    def add_line(self, text):
        """Return true if detected end if section."""
        for i in self.skiplines:
            if text.endswith(i):
                return

        words = text.split()
        if len(words) == 3:
            if (words[0] == 'Hide') and is_href(words[2]):
                return

        if text.startswith('Read ') and text.endswith(' More '):
            self.add_readmore(text)
        else:
            if text.strip():
                self.lines.append(clear_links(text))

    def add_readmore(self, text):
        """Line with read more link."""
        words = text.split()
        self.read_more = "[Read more]({})".format(words[1])


def start(_subj, body):
    """Parse Reddit message."""
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

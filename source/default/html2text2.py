# pylint: disable=W0223
"""Html parser ver2."""
from re import sub
from html.parser import HTMLParser
from html import unescape


class Parser(HTMLParser):
    """Parser class."""

    def __init__(self, extract_link, html_table):
        """Parser instance."""
        super().__init__()
        self.extract_link = extract_link
        self.html_table = html_table
        self.is_skip = False
        self.__text = []
        self.html_link = ''

    def extract_real_link(self, text):
        """Extract real link from redirects.

        Can be redifened in child classes.
        """
        return text

    def handle_data(self, data):
        """Process data."""
        if self.is_skip:
            self.is_skip = False
            return

        txt = data.strip()
        if txt:
            text = sub('[\t\r\n]+', '', txt)
            self.__text.append(text + ' ')

            if self.html_link:
                self.__text.extend([self.html_link, ' '])

            self.html_link = ''

    def handle_starttag(self, tag, attrs):
        """Start tags processing."""
        if tag == 'style':
            self.is_skip = True

        elif tag in ['p', 'br']:
            self.__text.append('\n')

        elif tag == 'a':
            if self.extract_link:
                link = self.extract_real_link(dict(attrs).get('href', '').strip())
                if link.startswith('http'):
                    self.html_link = link

        elif tag in ['table', 'tr', 'th', 'td']:
            if self.html_table:
                self.__text.append('\n')

    def handle_endtag(self, tag):
        """End tags processing."""
        if tag == 'style':
            self.is_skip = False

    @staticmethod
    def drop_newlines(text):
        """Drop extra mew lines from text."""
        while '\n\n\n' in text:
            text = text.replace('\n\n\n', '\n\n')

        return text

    def text(self):
        """Return result of parsing."""
        return self.drop_newlines(''.join(self.__text).strip())


def convert(parser_class, text, extract_link=False, html_table=True):
    """Parser call."""
    parser = parser_class(extract_link, html_table)
    parser.feed(unescape(text))
    parser.close()
    return parser.text()

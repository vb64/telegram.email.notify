# pylint: disable=W0223
"""Html parser."""
from re import sub
from html.parser import HTMLParser


class _DeHTMLParser(HTMLParser):
    """Parser class."""

    def __init__(self, extract_link):
        """Parser instance."""
        super().__init__()
        self.extract_link = extract_link
        self.is_skip = False
        self.__text = []
        self.html_link = ''

    def handle_data(self, data):
        """Data handker."""
        if self.is_skip:
            self.is_skip = False
            return

        text = data.strip()
        if text:
            text = sub('[\t\r\n]+', '', text)
            self.__text.append(text + ' ')
            if self.html_link:
                self.__text.append(self.html_link)
                self.__text.append(' ')

        self.html_link = ''

    def handle_starttag(self, tag, attrs):
        """Tag start."""
        if tag in ['p', 'br']:
            self.__text.append('\n')
        elif tag == 'style':
            self.is_skip = True
        elif tag == 'a':
            if self.extract_link:
                link = dict(attrs).get('href', '')
                if link.startswith('http'):
                    self.html_link = link

    def text(self):
        """Result of parsing."""
        return ''.join(self.__text).strip()


def convert(text, extract_link=False):
    """Parser call."""
    try:
        parser = _DeHTMLParser(extract_link)
        parser.feed(text)
        parser.close()

        return parser.text()

    except Exception:  # pragma: no cover pylint: disable=broad-except
        return sub(r'<.+?>', '', text)

# -*- coding: utf-8 -*-
"""
make test T=test_html2text.py
"""
from . import TestCase


class TestCaseHtml2text(TestCase):
    """
    Extraction text from html
    """
    def test_convert(self):
        """
        convert function
        """
        from html2text import convert

        html = ''.join((
          '<div dir="ltr">',
          'To: <a href="mailto:post@telegram-email.appspotmail.com">post@telegram-email.appspotmail.com</a>',
          '<br><br><br>to be or not to be?<br><br>',
          '###buttons<br>',
          'yes no maybe<br>option 3 option 4 option 5<br>option 6 option 7 option 8<br>',
          'option 9 option 10 option 11<br><br>',
          '{0001F1EC}{0001F1E7} Google  {0001F1F7}{0001F1FA} Yandex<div><br><br>',
          '-- <br>WBR, Vitaly<br></div></div>',
        ))
        text = convert(html)
        self.assertIn('post@telegram-email.appspotmail.com', text)

        html = self.get_fixture("msg03.html")
        text = convert(html)
        self.assertNotEqual(text, html)

    @staticmethod
    def test_convert_trunc():
        """
        convert trunc html
        """
        from html2text import convert

        html = ''.join((
          '<div>Пожалуйста, <a href=https://mail.yandex.ru/forward-confirm?',
          'e=SByzrmP%2bblW5URy3IVOBWeUMBTjbV2yYb5Q1swEsFJkfYpjiN7P%2bYZcXqR9YKdsF>подтвердите</a> ',
          'пересылку новых писем с vit-sar68@yandex.ru на Ваш адрес.<br />',
          'Если пересылка не нужна, проигнорируйте это письмо.</div>',
        ))
        text = convert(html)
        assert text

    def test_ampersand(self):
        """
        with ampersand
        """
        from html2text import convert

        link = ''.join((
          'https://mail.ukr.net/api/public/confirm_forwarding',
          '?e=vitalybogomolov@ukr.net&c=F6119539429&l=ru',
        ))

        html = ''.join((
          '<a href=',
          '"https://mail.ukr.net/api/public/confirm_forwarding?e=vitalybogomolov@ukr.net&c=F6119539429&l=ru"',
          'style="color:#4680d7;">',
          'https://mail.ukr.net/api/public/confirm_forwarding?e=vitalybogomolov@ukr.net&c=F6119539429&l=ru',
          '</a>',
        ))
        text = convert(html)
        self.assertEqual(text[:20], link[:20])

        html = self.get_fixture("msg02.html")
        text = convert(html)
        # self.assertIn(link, text)

    def test_style(self):
        """
        inside style tag
        """
        from html2text import convert

        html = self.get_fixture("msg01.html")

        link = ''.join((
          'http://fishingclub.od.ua/forums/index.php?/topic/',
          '18936-%D0%B4%D1%8E%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9-%D0%BF%D1%80%D1%83%D0%B4/',
          '&do=findComment&comment=512296',
        ))

        text = convert(html)
        self.assertNotEqual(text, '')
        self.assertNotIn('#outlook a {padding:0;}', text)
        self.assertNotIn(link, text)

        text = convert(html, extract_link=True)
        self.assertIn(link, text)

"""Ok.ru.

make test T=test_default/test_modules/test_ok.py
"""
from . import TestModule


class TestOk(TestModule):
    """Odnoklassniki.ru."""

    mark = "<html>"

    def transfer(self, fname):
        """Transfer fixture by ok."""
        from modules.ok import start
        return self.start_transfer(fname, start, 'ok')

    @staticmethod
    def test_make_link():
        """Check make_link."""
        from modules.ok import make_link, MARK_PROFILE_REF, SUBJ_POST

        txt = SUBJ_POST + MARK_PROFILE_REF
        ref = ''
        note = 'xxx'
        result = make_link(txt, ref, note)
        assert len(result) == 4

        txt = ''
        result = make_link(txt, ref, note)
        assert len(result) == 4

    def test_message(self):
        """Message."""
        text = self.transfer('no_photo.txt')
        assert self.mark not in text

        text = self.transfer('message.txt')
        assert self.mark not in text

    def test_m(self):
        """Check message N."""
        text = self.transfer('m1.txt')
        assert self.mark not in text

    def test_m2(self):
        """Check message m2."""
        text = self.transfer('m2.txt')
        assert self.mark not in text

    def test_present(self):
        """Present."""
        text = self.transfer('present1.txt')
        assert self.mark not in text

        text = self.transfer('present.txt')
        assert self.mark not in text

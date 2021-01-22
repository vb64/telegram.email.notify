"""
make test T=test_modules/test_ok.py
"""
from . import TestModule


class TestOk(TestModule):
    """
    Odnoklassniki.ru
    """
    mark = "<html>"

    def transfer(self, fname):
        """
        transfer fixture by ok
        """
        from modules.ok import start
        return self.start_transfer(fname, start, 'ok')

    @staticmethod
    def test_make_link():
        """
        make_link
        """
        from modules.ok import make_link, MARK_PROFILE_REF, SUBJ_POST

        txt = SUBJ_POST + MARK_PROFILE_REF
        ref = ''
        note = 'xxx'
        result = make_link(txt, ref, note)
        assert result

    def test_message(self):
        """
        message
        """
        text = self.transfer('no_photo.txt')
        assert self.mark not in text

        text = self.transfer('message.txt')
        assert self.mark not in text

    def test_m(self):
        """
        mN
        """
        text = self.transfer('m1.txt')
        assert self.mark not in text

    def test_m2(self):
        """
        m2
        """
        text = self.transfer('m2.txt')
        assert self.mark not in text

    def test_present(self):
        """
        present
        """
        text = self.transfer('present1.txt')
        assert self.mark not in text

        text = self.transfer('present.txt')
        assert self.mark not in text
        # print "###"
        # print text

import logging
from . import ecode

fb_url = "https://www.facebook.com/"
mark = "Facebook {}".format(fb_url)


def start(text):
    source = ecode(text)
    logging.info("facebook.ru:\n{}".format(source))

    i = source.find(mark)
    if i == -1:
        return source

    link = ''
    text = source[i + len(mark):]
    j = text.find('&aref=')
    if j > 0:
        text = text[:j]
        if ('groups' in text) and ('permalink' in text):
            text = text.split('%2F')
            link = "{}groups/{}/permalink/{}/".format(fb_url, text[1], text[3])

    text = ' '.join(source[:i].rstrip().split()[:-2])

    if text.startswith('['):
        i = text.find(']')
        if i > 0:
            title = text[1:i]
            j = text.find(title, i)
            if j > 0:
                text = text[j + len(title):].strip()
                if text.startswith('.'):
                    text = text[1:].strip()
                text = "Facebook {}\n\n{}".format(title, text)

    if link:
        text = "{}\n\n###buttons\n[Facebook]({})".format(text, link)

    # print text.decode('utf-8').encode('cp866')
    logging.info("result:\n{}".format(text))

    return text

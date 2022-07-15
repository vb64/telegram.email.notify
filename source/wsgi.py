"""
App endpoint handlers
"""
import importlib

from google.appengine.ext import blobstore
from flask import render_template, request, make_response, abort, Flask
from models import EmailData

app = Flask(__name__)  # pylint: disable=invalid-name

CODECS = {
  'ym': "Yandex Money",
  'youtube': "YouTube",
  'fb': "FaceBook",
  'ok': 'Odnoklassniki.ru',
  'twitter': "Twitter",
  'reddit': "Reddit",
  'lj': 'LiveJournal',
  'beeline': 'Beeline',
  'galerts': 'Google Alerts',
  'subjonly': 'Subject only',
  # not implemented handlers, just store message to db
  'store': None,
}


def run(codec, body):
    """
    run codec for transform body
    """
    if body == 'testdata':
        response = make_response('OK')
        response.mimetype = "text/plain"
        return response

    lines = body.splitlines()
    subj = lines[0]
    text = '\n'.join(lines[1:])

    try:
        if CODECS[codec] is None:
            from modules import store
            ret = store(codec, subj, text)
        else:
            pmod = importlib.import_module("modules.{}".format(codec))
            ret = pmod.start(subj, text)

    except Exception:
        from models import SavedSource
        SavedSource(label=codec, subject=subj, body=text).put()
        raise

    response = make_response(ret)
    response.mimetype = "text/plain"
    return response


@app.route('/', methods=['GET', 'POST'])
def mainpage():
    """
    root page
    """
    context = {
      'upload_url': blobstore.create_upload_url('/upload/'),
    }
    return render_template('main.html', **context)


@app.route('/email/<eid>/', methods=['GET', 'POST'])
def email_view(eid):
    """
    view data for email with given ID
    """
    edata = EmailData.get_by_id(int(eid))
    if not edata:
        return abort(404)

    if request.method == 'POST':
        text = '\n'.join((edata.field_subj, edata.field_text, edata.field_html))
        return run(
          request.form.get('codec'),
          text.encode('utf-8')
        )

    context = {
      'edata': edata,
      'codecs': CODECS,
    }
    return render_template('email_view.html', **context)


@app.route('/transform/<codec>/', methods=['POST'])
def transform(codec):
    """
    transform post
    """
    if codec not in CODECS:
        return abort(404)

    return run(codec, request.get_data())


@app.route('/_ah/warmup')
def warmup():
    """
    handle warmup request to suppress  warning into logs
    """
    return 'OK'


@app.route('/_ah/start')
def backend_start():
    """
    handle backend start request to suppress  warning into logs
    """
    return 'OK'

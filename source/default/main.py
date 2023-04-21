"""App endpoint handlers."""
import os
import importlib
from flask import render_template, request, make_response, abort, Flask, redirect
from google.appengine.api import wrap_wsgi_app
from models import EmailData

app = Flask(__name__)  # pylint: disable=invalid-name

# https://cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app?tab=python
if os.getenv('GAE_ENV', '').startswith('standard'):  # pragma: no cover
    # Production in the standard environment
    app.wsgi_app = wrap_wsgi_app(app.wsgi_app)

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
    """Run codec for transform body."""
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
    """Root page."""
    context = {
      'upload_url': '/upload/',
    }
    return render_template('main.html', **context)


@app.route('/upload/', methods=['POST'])
def upload():
    """GAE upload handler."""
    if 'emailbody' not in request.files:
        return redirect('/')

    try:
        edata = EmailData.from_upload(request.files['emailbody'])
    except AttributeError:
        return redirect('/')

    return redirect('/email/{}/'.format(edata.key.id()))


@app.route('/email/<eid>/', methods=['GET', 'POST'])
def email_view(eid):
    """View data for email with given ID."""
    edata = EmailData.get_by_id(int(eid))
    if not edata:
        return abort(404)

    if request.method == 'POST':
        text = '\n'.join((edata.field_subj, edata.field_text, edata.field_html))
        return run(request.form.get('codec'), text)

    context = {
      'edata': edata,
      'codecs': CODECS,
    }
    return render_template('email_view.html', **context)


@app.route('/transform/<codec>/', methods=['POST'])
def transform(codec):
    """Transform post."""
    if codec not in CODECS:
        return abort(404)

    return run(codec, request.get_data(as_text=True))

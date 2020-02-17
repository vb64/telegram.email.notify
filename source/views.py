"""
App endpoint handlers
"""
import logging
import importlib
from flask import render_template, request, make_response, abort
from wsgi import app

CODECS = {
  'ym': "Yandex Money",
  'fb': "FaceBook",
  'youtube': "YouTube",
}


def run(codec, body):
    """
    run codec for transform body
    """
    if isinstance(body, unicode):
        body = body.encode('utf8')

    lines = body.splitlines()
    subj = lines[0]
    text = '\n'.join(lines[1:])

    logging.info(codec)
    logging.info(subj)
    logging.info(text)

    pmod = importlib.import_module("modules.{}".format(codec))
    response = make_response(pmod.start(subj, text))
    response.mimetype = "text/plain"
    return response


@app.route('/', methods=['GET', 'POST'])
def mainpage():
    """
    root page
    """
    if request.method == 'POST':
        return run(request.form.get('codec'), request.form.get('source'))

    context = {
      'codecs': CODECS,
    }
    return render_template('main.html', **context)


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

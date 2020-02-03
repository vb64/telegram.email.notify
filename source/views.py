"""
App endpoint handlers
"""
import logging
import importlib
from flask import render_template, request, make_response, abort
from wsgi import app

CODECS = {
  'ym': "Yandex Money",
}


@app.route('/', methods=['GET', 'POST'])
def mainpage():
    """
    root page
    """
    if request.method == 'POST':
        pmod = importlib.import_module("modules.{}".format(request.form.get('codec')))
        response = make_response(pmod.start(request.form.get('source')))
        response.mimetype = "text/plain"
        return response

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

    text = request.get_data()
    logging.info(codec)
    logging.info(text)

    pmod = importlib.import_module("modules.{}".format(codec))
    response = make_response(pmod.start(text))
    response.mimetype = "text/plain"
    return response


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

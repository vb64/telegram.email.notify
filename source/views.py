"""
App endpoint handlers
"""
import importlib
from flask import render_template, request, make_response
from wsgi import app


@app.route('/_ah/warmup')
def warmup():
    """
    warmup request
    """
    return 'OK'


@app.route('/_ah/start')
def backend_start():
    """
    backend start request
    """
    return 'OK'


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
      'codecs': {'ym': "Yandex Money"},
    }
    return render_template('main.html', **context)

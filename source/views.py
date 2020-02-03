"""
App endpoint handlers
"""
from flask import render_template
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


@app.route('/')
def mainpage():
    """
    root page
    """
    context = {
      'codecs': {'ym': "Yandex Money"},
    }
    return render_template('main.html', **context)

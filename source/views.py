"""
App endpoint handlers
"""
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


@app.route('/', methods=['GET'])
def mainpage():
    """
    root page
    """
    context = {
      'codecs': {'ym': "Yandex Money"},
    }
    return render_template('main.html', **context)


@app.route('/', methods=['POST'])
def transform():
    """
    root page
    """
    response = make_response("codec: {}\n\nsource:\n{}".format(
      request.form['codecs'],
      request.form['source']
    ))
    response.mimetype = "text/plain"
    return response

"""
App endpoint handlers
"""
from flask import render_template, request
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
        return "codec: {}\n\nsource:\n{}".format(
          request.form['codecs'],
          request.form['source']
        )

    context = {
      'codecs': {'ym': "Yandex Money"},
    }
    return render_template('main.html', **context)

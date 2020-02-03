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


@app.route('/', methods=['GET', 'POST'])
def mainpage():
    """
    root page
    """
    if request.method == 'POST':
        response = make_response(u"codec: {}\n\nsource:\n{}".format(
          request.form.get('codec'),
          request.form.get('source')
        ))
        response.mimetype = "text/plain"
        return response

    context = {
      'codecs': {'ym': "Yandex Money"},
    }
    return render_template('main.html', **context)

"""Backend GAE service."""
from datetime import datetime, timedelta
import logging
from flask import Flask
from google.appengine.ext import ndb
from google.appengine.api import wrap_wsgi_app

PORTION = 500
PARTS = 10
DAYS_OLD = 30

app = Flask(__name__)
app.wsgi_app = wrap_wsgi_app(app.wsgi_app)


class SavedSource(ndb.Model):
    """Source of inbound requests."""

    made = ndb.DateTimeProperty()


class EmailData(ndb.Model):
    """Email origin file data."""

    made = ndb.DateTimeProperty()


def purge_model(model_class, border_date):
    """Purge ndb model of the given class."""
    count = 0
    query = model_class.query(model_class.made < border_date)

    for _i in range(PARTS):
        keys = query.fetch(PORTION, keys_only=True)
        if not keys:
            return count
        count += len(keys)
        ndb.model.delete_multi(keys)

    logging.warning("### Table '%s'. Deleted: %s", model_class.__name__, count)
    return count


@app.route('/')
def main():
    """Purge ndb models EmailData and SavedSource."""
    border_date = datetime.utcnow() - timedelta(days=DAYS_OLD)
    count_email = purge_model(EmailData, border_date)
    count_source = purge_model(SavedSource, border_date)
    return "'EmailData' deleted: {} 'SavedSource' deleted: {}".format(count_email, count_source)


if __name__ == '__main__':  # pragma: no cover
    app.run(host='127.0.0.1', port=8080, debug=True)

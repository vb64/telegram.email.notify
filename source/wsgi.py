"""
Entry point for app
"""
from warnings import filterwarnings
from requests.packages.urllib3.contrib.appengine import AppEnginePlatformWarning  # noqa: E501 pylint: disable=import-error

filterwarnings('ignore', category=AppEnginePlatformWarning)

import requests  # noqa: F401 pylint: disable=wrong-import-position,unused-import,ungrouped-imports
from requests_toolbelt.adapters import appengine  # noqa: F401 pylint: disable=wrong-import-position
from flask import Flask  # noqa: F401 pylint: disable=wrong-import-position

# Use the App Engine Requests adapter. This makes sure that Requests uses URLFetch.
appengine.monkeypatch()
app = Flask(__name__)  # pylint: disable=invalid-name

import views  # noqa: F401,E402 pylint: disable=wrong-import-position,unused-import

"""
Entry point for app
"""
from flask import Flask

app = Flask(__name__)  # pylint: disable=invalid-name

import views  # noqa: F401,E402 pylint: disable=wrong-import-position,unused-import

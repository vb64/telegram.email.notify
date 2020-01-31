"""
Configuration file for external libraries
"""
import os
from google.appengine.ext import vendor

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
vendor.add(os.path.join(PROJECT_DIR, 'libs'))

"""
WSGI Entry Point
"""
import os
from btvpython.webapp import create_app
import run

application = run_app()

if 'FLASK_DEBUG' in os.environ:
    application.debug = True
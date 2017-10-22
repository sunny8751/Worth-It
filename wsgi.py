"""
WSGI Entry Point
"""
import os
from btvpython.webapp import create_app

application = create_app()

if 'FLASK_DEBUG' in os.environ:
    application.debug = True
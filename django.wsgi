import os
import os.path
import sys

PATH = os.path.dirname(os.path.realpath(__file__))
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

if PATH not in sys.path:
    sys.path.insert(0, PATH)

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
#!/usr/bin/local/python3.6
import django

import os
import sys


path='/home/drake/mysite'

if path not in sys.path:
  sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
django.setup()


import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

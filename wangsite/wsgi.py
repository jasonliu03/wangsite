"""
WSGI config for wangsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys
print sys.path
sys.path.append("/usr/lib64/python2.7/site-packages")
sys.path.append("/usr/lib/python2.7/site-packages")
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wangsite.settings")

application = get_wsgi_application()

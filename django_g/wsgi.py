"""
WSGI config for django_g project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_g.settings')

import gevent.monkey
gevent.monkey.patch_all()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

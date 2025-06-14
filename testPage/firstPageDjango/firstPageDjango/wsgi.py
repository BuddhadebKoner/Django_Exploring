"""
WSGI config for firstPageDjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstPageDjango.settings')

application = get_wsgi_application()

# Vercel requires the WSGI application to be exposed as 'app'
app = application

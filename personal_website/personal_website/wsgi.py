"""
WSGI config for personal_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""



import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append ('/vagrant/personal_website')
sys.path.append ('/vagrant')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personal_website.settings")
application= get_wsgi_application()

#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()





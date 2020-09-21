"""
WSGI config for durumi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "durumi.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'durumi.settings')
>>>>>>> eight-b1

application = get_wsgi_application()

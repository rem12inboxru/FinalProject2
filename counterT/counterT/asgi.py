"""
ASGI config for counterT project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django_tortoise import get_boosted_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'counterT.settings')

application = get_asgi_application()

application = get_boosted_asgi_application(application)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'counterT.settings')

#application = get_asgi_application()

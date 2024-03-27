"""
WSGI config for chint project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from config import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chint.settings')

application = get_wsgi_application()

if ENVIRONMENT == 'local' and TELEGRAM_BOT_API_TOKEN:
    from bot.update import updater
    # updater.start_polling()
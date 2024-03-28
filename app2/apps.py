from django.apps import AppConfig
from django.conf import settings
import os

class app2(AppConfig):
    name = 'app2'
    path = os.path.join(settings.BASE_DIR, 'app2')
    def ready(self):
        # from app.models import About, Rule
        # About.objects.get_or_create(pk=1)
        # Rule.objects.get_or_create(pk=1)
        return super().ready()

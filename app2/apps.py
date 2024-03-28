from django.apps import AppConfig

class app2(AppConfig):
    name = 'app2'

    def ready(self):
        # from app.models import About, Rule
        # About.objects.get_or_create(pk=1)
        # Rule.objects.get_or_create(pk=1)
        return super().ready()

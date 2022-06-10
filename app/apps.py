from django.apps import AppConfig

class app(AppConfig):
    name = 'app'

    def ready(self):
        # from app.models import About, Rule
        # About.objects.get_or_create(pk=1)
        # Rule.objects.get_or_create(pk=1)
        return super().ready()

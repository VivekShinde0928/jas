from django.apps import AppConfig


class JasAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jas_app'

    def ready(self):
        import jas_app.signals

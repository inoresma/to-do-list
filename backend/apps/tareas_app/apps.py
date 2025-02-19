from django.apps import AppConfig


class TareasAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.tareas_app'

    def ready(self):
        import apps.tareas_app.utils

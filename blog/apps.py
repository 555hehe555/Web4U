from django.apps import AppConfig
import sys

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        # Запускаємо тільки при `runserver`
        if 'runserver' in sys.argv and not ('makemigrations' in sys.argv or 'migrate' in sys.argv):
            from create_superuser import create_superuser  # ← шлях до твого скрипта
            create_superuser()

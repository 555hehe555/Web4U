from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.db.utils import OperationalError

class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        from django.contrib.auth import get_user_model

        def create_superuser(sender, **kwargs):
            User = get_user_model()
            try:
                if not User.objects.filter(is_superuser=True).exists():
                    User.objects.create_superuser(
                        username="admin",
                        email='admin@example.com',
                        password='admin123'
                    )
            except OperationalError:
                pass

        post_migrate.connect(create_superuser, sender=self)

from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.db.utils import OperationalError

class BlogApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_api'
    
    def ready(self):
        from django.contrib.auth import get_user_model

        def create_users(sender, **kwargs):
            User = get_user_model()
            try:
                # Суперкористувач
                if not User.objects.filter(is_superuser=True).exists():
                    User.objects.create_superuser(
                        username="admin",
                        email='admin@example.com',
                        password='admin'
                    )

                # Звичайний користувач
                if not User.objects.filter(username="user").exists():
                    User.objects.create_user(
                        username="user",
                        email='user@example.com',
                        password='user'
                    )

            except OperationalError:
                pass

        post_migrate.connect(create_users, sender=self)

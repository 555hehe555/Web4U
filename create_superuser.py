from django.contrib.auth import get_user_model
import os

User = get_user_model()
# username = "admin"
# email = "admin@example.com"
# password = "admin123"
username = os.getenv("ADMIN_NAME", "admin")
email = os.getenv("ADMIN_EMAIL", "admin@localhost")
password = os.getenv("ADMIN_PASSWORD", "admin")

def create_superuser():
    """
    Create a superuser if it does not already exist.
    """
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Superuser created.")
    else:
        print("Superuser already exists.")


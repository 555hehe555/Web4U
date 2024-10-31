import os

def create_superuser():
    """Run the createsuperuser command in a new command line window."""
    print("Creating superuser...")
    os.system("start cmd /k venv\\Scripts\\python manage.py createsuperuser")

if __name__ == "__main__":
    create_superuser()

import subprocess


def run_server():
    """Run the Django development server."""
    subprocess.run(r"venv\Scripts\python manage.py runserver", shell=True)


if __name__ == "__main__":
    run_server()

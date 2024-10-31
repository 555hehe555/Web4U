import subprocess
import webbrowser


def run_server():
    """Run the Django development server."""
    subprocess.run(r"venv\Scripts\python manage.py runserver", shell=True)

    webbrowser.open("http://127.0.0.1:8000/")

if __name__ == "__main__":
    run_server()

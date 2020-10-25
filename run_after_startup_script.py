import os
import logging

logger = logging.getLogger(__name__)


def run_on_startup():
    os.system("pip install -r requirements.txt --upgrade")
    # importing it here to make sure Django gets installed first
    from django.core.management.utils import get_random_secret_key
    from django.core.management import execute_from_command_line

    os.system(">.env")
    with open(".env", "w+") as f:
        f.write("SECRET_KEY={}".format(get_random_secret_key()))
    os.system("pre-commit install")
    execute_from_command_line(["manage.py", "migrate"])


if __name__ == "__main__":
    run_on_startup()

"""
RUN THIS FILE WHEN THE NEW APP IS CREATED
"""

import os
import logging

logger = logging.getLogger(__name__)


def run_on_startup():
    os.system("pip install -r requirements.txt --upgrade")
    # importing it here to make sure Django gets installed first
    from django.core.management.utils import get_random_secret_key
    os.system(">readme.md")
    os.system(">.env")
    with open(".env", "w+") as f:
        f.write("SECRET_KEY={}".format(get_random_secret_key()))
    os.system('rm -rf .git')
    os.system('git init')
    os.system("pre-commit install")
    with open(".gitignore","a") as f:
        f.write('startup_script.py')
        f.write('\n')
        f.write('run_after_startup_script.py')


if __name__ == "__main__":
    run_on_startup()

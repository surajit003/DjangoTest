import os
import fnmatch
import pathlib
import logging

logger = logging.getLogger(__name__)

CURRENT_PROJECT_NAME = "DjangoTest"
NEW_PROJECT_NAME = "DjangoTest"  # modify this line to your new project name


def replace_in_specific_file(filename, find, replace):
    try:
        with open(filename, "r") as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(find, replace)

        # Write the file out again
        with open(filename, "w") as file:
            file.write(filedata)
    except Exception as ex:
        logger.exception(ex)


def find_replace_recursively(directory, find, replace, filePattern):
    try:
        for path, dirs, files in os.walk(os.path.abspath(directory)):
            for filename in fnmatch.filter(files, filePattern):
                filepath = os.path.join(path, filename)
                with open(filepath) as f:
                    s = f.read()
                s = s.replace(find, replace)
                with open(filepath, "w") as f:
                    f.write(s)
    except Exception as ex:
        logger.exception(ex)


def rename_root_directory(path):
    for root, dirs, files in os.walk(path):
        for directory in dirs:
            new_path = str(path).replace(
                CURRENT_PROJECT_NAME, NEW_PROJECT_NAME
            )  # Full path of file whose name is changed
            os.rename(path, new_path)


def run_on_startup():
    full_path = pathlib.Path().absolute()
    current_directory = str(full_path).split("/")
    current_directory_name = current_directory[-1]
    if current_directory_name == CURRENT_PROJECT_NAME:
        # do stuffs for renaming
        # start by replacing CURRENT_PROJECT_NAME in urls.py,settings.py,wsgi.py,asgi.py
        django_app_path = "{}/{}".format(full_path, current_directory_name)
        file_pattern = "*.py"
        find_replace_recursively(
            django_app_path, CURRENT_PROJECT_NAME, NEW_PROJECT_NAME, file_pattern
        )
        try:
            os.rename(CURRENT_PROJECT_NAME, NEW_PROJECT_NAME)
        except FileNotFoundError as ex:
            logger.exception(ex)
        replace_in_specific_file("manage.py", CURRENT_PROJECT_NAME, NEW_PROJECT_NAME)
        rename_root_directory(full_path)


if __name__ == "__main__":
    run_on_startup()

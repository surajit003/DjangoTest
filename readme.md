Instead of doing the repetitive work for initial Django set up, I have boostrapped this
project to help with the initial set up.

This is tested on Linux based systems

To start everything, clone the project locally https://github.com/surajit003/DummyDjangoApp.git

1. A file called startup_script.py is already in the root folder.Inside it, you will simply need to make a one line modification to your desired project
name NEW_PROJECT_NAME = "DjangoTest"
2. Activate virtual environment.
3. Simply run python startup_script.py and Voila.

The initial set up comes with the following
1. python-decouple package for settings configs
2. pre-commit hook config
3. black which is run by pre-commit hook everytime you push a commit
5. .gitignore file
6. requirement file for all pip packages to be installed

Once the new project is set up, simply run python3 run_after_startup_script.py and it will do the following
1.Install basic pip packages such as Django, Black, pre-commit hook.
2.Set up env file and auto generate Django SECRET key.

That's it.

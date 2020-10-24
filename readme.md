Instead of doing the repetitive work for initial Django set up, I have boostrapped this
project to help with the initial set up.

This is tested on Linux based systems

To start everything, clone the project locally https://github.com/surajit003/DummyDjangoApp.git

A file called startup_script.py is already in the root folder
Inside it, you will simply need to make a one line modification to your desired project
name
NEW_PROJECT_NAME = "DjangoTest"
Change NEW_PROJECT_NAME value to the project you want to rename
Then simply run python startup_script.py and Voila. 

The initial set up comes with the following
1. python-decouple package for settings configs
2. pre-commit hook config
3. black which is run by pre-commit hook everytime you push a commit
4. .env file with dynamic DJANGO SECRET_KEY
5. .gitignore file
6. requirement file for all pip packages already installed when you run startup script


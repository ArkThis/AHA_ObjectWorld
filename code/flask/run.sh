#!/bin/bash

# before this, run:
#  source $dir_to_my_python_virtual_environment/my_venv

PORT=5000
export FLASK_APP=hello_world/hello
export FLASK_ENV=development

flask run -p $PORT

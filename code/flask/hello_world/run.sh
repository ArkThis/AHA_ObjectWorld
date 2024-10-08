#!/bin/bash

# before this, run:
#  source $dir_to_my_python_virtual_environment/my_venv

OWNDIR=$(dirname $0)

PORT=5000
export FLASK_APP=$OWNDIR/hello
export FLASK_ENV=development

flask run -p $PORT

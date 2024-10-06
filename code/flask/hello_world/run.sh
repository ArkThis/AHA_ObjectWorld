#!/bin/bash

PORT=5000
export FLASK_APP=hello
export FLASK_ENV=development

flask run -p $PORT

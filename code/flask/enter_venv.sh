#!/bin/bash

DIR=$(dirname $0)
PROFILE="my_env"

echo ""
echo "Simon says:"
echo "(Run this to enter '$PROFILE' python virtual environment)"
echo ""
CMD="source $DIR/venv/$PROFILE/bin/activate"
echo "$CMD"

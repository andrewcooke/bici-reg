#!/bin/bash

cd "${BASH_SOURCE%/*}/" || exit 1
./assert-bcpasswd.sh || exit 2
pushd ..
source venv/bin/activate
PYTHONPATH=. flask --app bici_reg/server.py run



#!/bin/bash

cd "${BASH_SOURCE%/*}/" || exit 1
pushd ..
source venv/bin/activate
PYTHONPATH=. flask --app bici_reg/server.py run



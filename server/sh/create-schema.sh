#!/bin/bash

cd "${BASH_SOURCE%/*}/" || exit 1
./assert-bcpasswd.sh || exit 3
pushd ..
source venv/bin/activate
PYTHONPATH=. python bici_reg/create-schema.py


#!/bin/bash

cd "${BASH_SOURCE%/*}/" || exit 1
pushd ..
source venv/bin/activate
python -c 'import secrets; print(secrets.token_hex())'


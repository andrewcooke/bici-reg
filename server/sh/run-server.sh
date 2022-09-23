#!/bin/bash

cd "${BASH_SOURCE%/*}/" || exit 1
./assert-env.sh || exit 2
pushd ..
source venv/bin/activate
python -m bici_reg.server



#!/bin/bash

cd "${BASH_SOURCE%/*}/" || exit
cd ..
rm -fr venv
python3.10 -m venv venv
source venv/bin/activate
pip install pip --upgrade
pip install flask
pip install sqlalchemy
pip install flask-sqlalchemy
pip install psycopg2-binary
pip install flask-login

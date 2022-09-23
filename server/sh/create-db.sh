#!/bin/bash

cd "${BASH_SOURCE%/*}/" || exit 1
./assert-env.sh || exit 2
PGPASSWORD=$PGPASSWD psql -U postgres -h localhost -c "create user bici with password '$BCPASSWD'"
PGPASSWORD=$PGPASSWD psql -U postgres -h localhost -c "create database bici with owner bici"

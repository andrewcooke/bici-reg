#!/bin/bash

cd "${BASH_SOURCE%/*}/" || exit 1
./assert-env.sh || exit 2
./start-postgres.sh
echo "waiting for postgres to start"
sleep 10
./create-db.sh
./create-schema.sh

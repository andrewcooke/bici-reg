#!/bin/bash

cd "${BASH_SOURCE%/*}/" || exit 1
./assert-pgpasswd.sh || exit 2
./assert-bcpasswd.sh || exit 3
./start-postgres.sh
echo "waiting for postgres to start"
sleep 10
./create-db.sh
./create-schema.sh

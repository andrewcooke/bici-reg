#!/bin/bash

cd "${BASH_SOURCE%/*}/" || exit 1
./assert-env.sh || exit 2
docker run --rm --name postgres -p 5432:5432 -e POSTGRES_PASSWORD="$PGPASSWD" -d postgres

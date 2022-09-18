#!/bin/bash

cd "${BASH_SOURCE%/*}/" || exit 1
./assert-pgpasswd.sh || exit 2
./assert-bcpasswd.sh || exit 3
PGPASSORD=$PGPASSWD psql -U postgres -h localhost -c "create user bici with password '$BCPASSWD'"

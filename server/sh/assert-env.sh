#!/bin/bash

for name in BCPASSWD PGPASSWD SECRET_KEY PASSWORD_SALT; do
    if [ -z "${!name}" ]; then
	echo "$name must be defined in the environment"
	exit 1
    fi
done

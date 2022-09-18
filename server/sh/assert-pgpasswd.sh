#!/bin/bash

if [ -z "$PGPASSWD" ]; then
    echo "PGPASSWD must be defined in the environment"
    exit 1
fi

#!/bin/bash

if [ -z "$BCPASSWD" ]; then
    echo "BCPASSWD must be defined in the environment"
    exit 1
fi

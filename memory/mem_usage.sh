#!/bin/bash

if [ -z "$1" ]; then
    echo "Error: One parameter (process PID) required!"
    exit 1
fi

awk -f mem.awk /proc/$1/smaps


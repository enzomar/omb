#!/bin/bash

swd=$(dirname "$0")

phase=$(head -n 1 ${swd}/../.phase 2> /dev/null)
if [ -z $phase ]; then
    exit 1
fi
echo $phase
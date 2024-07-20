#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

url=$1
curl -I -L "$url" 2> /dev/null | grep -m 1 "Location" | cut -d ' ' -f 2

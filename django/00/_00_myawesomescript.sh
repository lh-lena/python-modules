#!/bin/sh

# allowed functions: curl, grep, cut

if [ -z "$1" ]; then
    echo "Invalid input. Usage: $0 bit.ly/[url]"
    exit 1
fi

res=$(curl -Ls -D - "$1" -o /dev/null | grep "Location" | cut -c 11-)

echo $res

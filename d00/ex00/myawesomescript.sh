#!/bin/sh

### Execute script
#

## Check if there is only one argument
if [ $# = 1 ]; then

	## Execute the curl command
	curl -Is $1 | grep 'Location' | cut -d' ' -f2

## There is too less/much argument
else
	exit 1
fi

#!/bin/bash
# Script that sends header var
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"

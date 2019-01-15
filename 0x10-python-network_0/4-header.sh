#!/bin/bash
# Script that sends header var
curl -s -X GET --header "X-HolbertonSchool-User-Id: 98" "$1"

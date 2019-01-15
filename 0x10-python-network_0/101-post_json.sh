#!/bin/bash
# SCript that send a JSON request
curl -s -X POST -H "Accept: application/json" -H "Content-Type: application/json" -d "@$2" $1

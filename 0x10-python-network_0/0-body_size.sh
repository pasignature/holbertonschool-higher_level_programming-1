#!/usr/bin/env bash
# Takes in a URL, sends a request, and displays the size of the body
curl -s -o /dev/null -sw "%{size_download}" "$1"; echo ""

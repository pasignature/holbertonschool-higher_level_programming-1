#!/bin/bash
# Script
curl -s -w "%{http_code}" -o /dev/null "$1"

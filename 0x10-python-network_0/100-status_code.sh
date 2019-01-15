#!/bin/bash
# Script
curl -sw "%{http_code}" -o /dev/null "$1"

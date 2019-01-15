#!/bin/bash
# Sends a POST request and displays response
curl -sd "email=hr@holbertonschool.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"

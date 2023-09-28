#!/usr/bin/env bash
# This script displays the size of the body of the response
curl -Is "$1" | grep -i "Content-Length:" | awk '{print $2}' | cut -d$'\n' -f1

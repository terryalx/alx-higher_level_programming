#!/bin/bash
# send request to url
curl -s "$1" | wc -c

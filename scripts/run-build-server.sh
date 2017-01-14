#/usr/bin/env bash

# Make pelican build on startup


echo "> Building Site"
pelican -v

echo "Starting Server"
npm start

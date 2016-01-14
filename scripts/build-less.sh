#!/usr/bin/env bash

set -e

if [[ $@ == prod ]]
then
  echo ">>> WARNING: Building in Production Mode!"
fi

echo ">> Building LESS..."
lessc --silent static/src/less/style.less static/build/css/style.css

if [[ $@ == prod ]]
then
  echo ">> Compressing LESS..."
  cleancss -d --s0 -o static/build/css/style.css static/build/css/style.css
fi

#!/usr/bin/env bash

set -e

mkdir -p static/build/js/lib static/build/fonts static/build/css static/build/img
cp -R node_modules/font-awesome/fonts static/build/
cp -R node_modules/bootstrap-sass/assets/fonts/* static/build/fonts
cp -R static/src/img static/build


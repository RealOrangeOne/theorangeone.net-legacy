#!/usr/bin/env bash

set -e

if [ "$NODE_ENV" = "production" ]
then
  echo ">>> WARNING: Building in Production Mode!"
fi

echo ">> Building SCSS..."
node-sass theme/static/src/scss/index.scss theme/static/build/css/index.css --source-map-embed

echo ">> Post-Processing..."
postcss -u autoprefixer -o theme/static/build/css/index.css theme/static/build/css/index.css

if [ "$NODE_ENV" = "production" ]
then
  echo ">> Compressing CSS..."
  cleancss -d --s0 -o theme/static/build/css/index.css theme/static/build/css/index.css
fi

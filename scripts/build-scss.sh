#!/usr/bin/env bash

set -e

if [ "$NODE_ENV" = "production" ]
then
  echo ">>> WARNING: Building in Production Mode!"
fi

echo ">> Generating Pygments styles..."
env/bin/pygmentize -S github -f html -a .highlight > static/src/scss/pygment.css

echo ">> Building SCSS..."
node-sass static/src/scss/index.scss static/build/css/index.css --source-map-embed

echo ">> Post-Processing..."
postcss -u autoprefixer -o static/build/css/index.css static/build/css/index.css

if [ "$NODE_ENV" = "production" ]
then
  echo ">> Compressing CSS..."
  cleancss -d --s0 -o static/build/css/index.css static/build/css/index.css
fi

#!/usr/bin/env bash

set -e

if [[ $@ == prod ]]
then
  echo ">>> WARNING: Building in Production Mode!"
fi

mkdir -p static/build/js/lib

if [[ $@ == prod ]]
then
  echo ">> Compressing Libraries..."
  uglifyjs node_modules/markdown/lib/markdown.js --compress --screw-ie8 --define --stats --keep-fnames -o static/build/js/lib/markdown.js
  uglifyjs node_modules/bootstrap/dist/js/bootstrap.js --compress --screw-ie8 --define --stats --keep-fnames -o static/build/js/lib/bootstrap.js
  uglifyjs static/build/js/lib/* --compress --screw-ie8 --define --stats --keep-fnames -o static/build/js/libs.js
else
  echo ">> Building Libraries..."
  cp node_modules/markdown/lib/markdown.js static/build/js/lib/markdown.js
  cp node_modules/bootstrap/dist/js/bootstrap.js static/build/js/lib/bootstrap.js
  uglifyjs static/build/js/lib/* --screw-ie8 --stats --keep-fnames -o static/build/js/libs.js
fi

rm -rf static/build/js/lib

if [[ $@ == prod ]]
then
  echo ">> Compressing jQuery..."
  uglifyjs node_modules/jquery/dist/jquery.js --compress --screw-ie8 --define --stats --keep-fnames -o static/build/js/jquery.js
else
  echo ">> Building jQuery..."
  cp node_modules/jquery/dist/jquery.js static/build/js/jquery.js
fi


echo ">> Building Application JS..."
browserify -t [ babelify --presets [ es2015 react ] ] static/src/js/app.js -o static/build/js/app.js

if [[ $@ == prod ]]
then
  echo ">> Compressing Application..."
  uglifyjs static/build/js/app.js --compress --screw-ie8 --define --stats --keep-fnames -o static/build/js/app.js
fi

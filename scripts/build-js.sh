#!/usr/bin/env bash

set -e

if [[ $BUILD_PRODUCTION ]]
then
  echo ">>> WARNING: Building in Production Mode!"
fi

mkdir -p theme/static/build/js/lib

if [[ $BUILD_PRODUCTION ]]
then
  echo ">> Compressing Libraries..."
  uglifyjs node_modules/bootstrap-sass/assets/javascripts/bootstrap.js --compress --screw-ie8 --define --stats --keep-fnames -o theme/static/build/js/lib/bootstrap.js
  uglifyjs theme/static/build/js/lib/* --compress --screw-ie8 --define --stats --keep-fnames -o theme/static/build/js/libs.js
else
  echo ">> Building Libraries..."
  cp node_modules/bootstrap-sass/assets/javascripts/bootstrap.js theme/static/build/js/lib/bootstrap.js
  uglifyjs theme/static/build/js/lib/* --screw-ie8 --stats --keep-fnames -o theme/static/build/js/libs.js
fi

rm -rf theme/static/build/js/lib

if [[ $BUILD_PRODUCTION ]]
then
  echo ">> Compressing jQuery..."
  uglifyjs node_modules/jquery/dist/jquery.js --compress --screw-ie8 --define --stats --keep-fnames -o theme/static/build/js/jquery.js
else
  echo ">> Building jQuery..."
  uglifyjs node_modules/jquery/dist/jquery.js --screw-ie8 --stats --keep-fnames -o theme/static/build/js/jquery.js
fi


echo ">> Building Application JS..."
browserify -t [ babelify --presets [ es2015 react ] ] theme/static/src/js/app.js -o theme/static/build/js/app.js

if [[ $BUILD_PRODUCTION ]]
then
  echo ">> Compressing Application..."
  uglifyjs theme/static/build/js/app.js --compress --screw-ie8 --define --stats --keep-fnames -o theme/static/build/js/app.js
fi

echo "> JS Built!"

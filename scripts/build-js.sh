#!/usr/bin/bash

set -e

echo ">> Building Libraries..."
mkdir static/build/js/lib
uglifyjs node_modules/markdown/lib/markdown.js --compress --screw-ie8 --define --stats --keep-fnames -o static/build/js/lib/markdown.js
uglifyjs node_modules/bootstrap/dist/js/bootstrap.js --compress --screw-ie8 --define --stats --keep-fnames -o static/build/js/lib/bootstrap.js
uglifyjs static/build/js/lib/* --compress --screw-ie8 --define --stats --keep-fnames -o static/build/js/libs.js
rm -rf static/build/js/lib

echo ">> Building JQuery..."
uglifyjs node_modules/jquery/dist/jquery.js --compress --screw-ie8 --define --stats --keep-fnames -o static/build/js/jquery.js

echo ">> Building Application JS..."
browserify -t reactify static/src/js/app.js -o static/build/js/app.js
# uglifyjs static/build/js/app.js --compress --screw-ie8 --define --stats --keep-fnames -o static/build/js/app.js
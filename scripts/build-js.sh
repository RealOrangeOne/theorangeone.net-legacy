#!/usr/bin/bash

set -e

cp node_modules/bootstrap/dist/js/bootstrap.js static/src/js/lib/
cp node_modules/skrollr/src/skrollr.js static/src/js/lib/

echo ">> Building Libraries..."
uglifyjs node_modules/jquery/dist/jquery.js --compress --screw-ie8 --define --stats --keep-fnames -o static/build/js/jquery.js
uglifyjs node_modules/markdown/lib/markdown.js --compress --screw-ie8 --define --stats --keep-fnames -o static/build/js/markdown.js
uglifyjs static/src/js/lib/* --compress --screw-ie8 --define --stats --keep-fnames -o static/build/js/libs.js

echo ">> Building Application JS..."
browserify -t reactify static/src/js/app.js -o static/build/js/app.js
# uglifyjs static/build/js/app.js --compress --screw-ie8 --define --stats --keep-fnames -o static/build/js/app.js

echo ">> Building Global Utilities..."
uglifyjs static/src/js/utils.js --compress --screw-ie8 --define --stats --keep-fnames -o static/build/js/utils.js

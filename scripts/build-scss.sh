#!/usr/bin/env bash

set -e

mkdir -p theme/static/src/scss/css

# scss can't import css, so copy them into src dir and change the extension!
cp node_modules/animate.css/animate.css theme/static/src/scss/css/animate.scss

node-sass theme/static/src/scss/index.scss theme/static/build/css/index.css --source-map-embed

# Cleanup
rm -rf theme/static/src/scss/css

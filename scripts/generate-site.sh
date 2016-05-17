#!/usr/bin/env bash

set -e

echo "> Creating Site..."

# Build the static data
echo ">> Building static data..."
npm run build

echo ">> Compiling site pages..."
pelican -v

echo "> Build complete."

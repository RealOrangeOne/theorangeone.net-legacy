#!/usr/bin/env bash

set -e

echo ">> Linting JSON Data..."
jsonlint -q data/projects.json


echo "> Extra tests passed!"

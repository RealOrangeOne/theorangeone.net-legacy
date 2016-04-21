#!/usr/bin/env bash

set -e


echo ">> Removing VirtualEnv..."
rm -rf env/

echo ">> Removing Node Modules..."
rm -rf node_modules/

echo ">> Removing Static Build Directory..."
rm -rf static/build/

echo "> Cleaning Complete."

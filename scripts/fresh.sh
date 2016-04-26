#!/usr/bin/env bash

set -e


echo ">> Removing VirtualEnv..."
rm -rf env/

echo ">> Removing Collected Static Files..."
rm -rf collected-static/

echo ">> Removing Private Data..."
rm -rf private/

echo ">> Removing Node Modules..."
rm -rf node_modules/

echo ">> Removing Static Build Directory..."
rm -rf static/build/

echo ">> Removing Stray Files and Folders..."
rm -rf htmlcov/ .coverage

echo "> Much Fresher!"

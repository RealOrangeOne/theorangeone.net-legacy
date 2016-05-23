#!/usr/bin/env bash

set -e

echo ">> Removing old Private Data..."
rm -rf private/

echo ">> Getting Private Data..."
git clone git@github.com:RealOrangeOne/theorangeone.net-site-private-data.git --branch master --single-branch private/

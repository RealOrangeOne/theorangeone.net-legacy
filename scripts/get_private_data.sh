#!/usr/bin/bash

set -e

echo ">> Removing old Private data..."
rm -rf private/*
mkdir private/
cd private/

echo ">> Cloning Private Repo..."
git clone git@bitbucket.org:TheOrangeOne/theorangeone.net-site-private-data.git


echo ">> That's it for now..."

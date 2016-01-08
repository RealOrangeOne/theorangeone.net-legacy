#!/usr/bin/env bash

set -e

RED='tput setaf 1'
NC='tput sgr 0'
YELLOW='tput setaf 3'
GREEN='tput setaf 2'

cd
echo "$($YELLOW)>> Fetching Repository...$($NC)"
ctf fetch RealOrangeOne/theorangeone.net v3 deployment
sleep 15
echo "$($YELLOW)>> Entering Project...$($NC)"
project_dir="$(\ls -1dt ./*/ | head -n 1)"
previous_dir = "$(\ls -1dt ./*/ | head -n 2)"
cd project_dira
echo "$($YELLOW)>> Building Project...$($NC)"
ctf project run build
ctf project run manage.py migrate
echo "$($YELLOW)>> Routing Project...$($NC)"
ident=$project_dir + ":development:web"
ctf router staging.theorangeone.net --ident %ident
echo "$($YELLOW)>> Destroying Previous Project...$($NC)"
cd -
cd previous_dir
ctf project stop
cd -
rm -rf previous_dir

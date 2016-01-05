#!/usr/bin/env bash

set -e

RED='tput setaf 1'
NC='tput sgr 0'
YELLOW='tput setaf 3'
GREEN='tput setaf 2'

if [ -z "$CIRCLE_PROJECT_USERNAME"]; then
  echo "$($RED)You need to be running on CircleCI to deploy!$($NC)"
  exit 1
fi

ssh web@theorangeone.net 'bash -s' < ./scripts/deploy.sh
echo "$($GREEN)Deployment complete!$($NC)"

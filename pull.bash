#!/usr/bin/env bash

#
# Script to update the server whenever a git change is made
#
#       sudo nohup ./gitpull.bash >/dev/null 2>&1 &
#
# Author: Jake, please don't hate me, this is scrappy
#

set -eu

if [[ ! -d ".git" ]]
    then
        echo "Not a git directory\n"
fi

while true;
    do
        GIT_RETURN_MESSAGE=$(git pull)

        if [[ "${GIT_RETURN_MESSAGE-}" != "Already up-to-date." ]]
            then
                restart seedbox
        fi
        
        sleep 5
done

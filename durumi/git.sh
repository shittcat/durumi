#! /bin/bash
#! ./git.sh

msg="$(date '+%m')$(date '+%d')_desktop"

git add .
git commit -m $msg
git push -u origin synod2-b3


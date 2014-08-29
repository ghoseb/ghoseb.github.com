#!/bin/bash
rsync -zrpt --delete --progress --force --delete-excluded --exclude=deploy.sh --exclude=.gitignore --exclude=.DS_Store --exclude=.git --exclude=.idea ~/Sites/functionalconf/ naresh@naresh.webfactional.com:/home/naresh/webapps/functionalconf/

#!/bin/bash

DIR = "/root/seamusic/seamusic-backend-prod"

if [ ! -d "$DIR" ]; then
  mkdir -p "$DIR"
else
  echo ""
fi

cd "$DIR" || exit

git pull origin master

make start

echo "Deployment completed successfully! 🎉"

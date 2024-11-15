#!/bin/bash

DIR = "/root/seamusic/seamusic-backend-dev"

if [ ! -d "$DIR" ]; then
  mkdir -p "$DIR"
else
  echo ""
fi

cd "$DIR" || exit

git pull origin dev

make start

echo "Deployment completed successfully! 🎉"

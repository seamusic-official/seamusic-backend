#!/bin/bash

DIR = "/root/seamusic/seamusic-backend-dev"

if [ ! -d "$DIR" ]; then
  mkdir -p "$DIR"
else
  echo ""
fi

cd "$DIR" || exit

git pull origin master

make start

# Сборка проекта (если это необходимо)
npm run build

# Перезапуск сервиса (например, через PM2 или systemd)
# Если ты используешь PM2
pm2 restart your-app-name

# Или если через systemd
# sudo systemctl restart your-service.service

echo "Deployment completed successfully! 🎉"

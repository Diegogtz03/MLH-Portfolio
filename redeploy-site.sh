#!/bin/bash

# cd into projects folder
cd /root/MLH-Portfolio

# git fetch
git fetch && git reset origin/main --hard

# Spin docker containers down to prevent errors
docker compose -f docker-compose.prod.yml down

# Compose docker containers back up
docker compose -f docker-compose.prod.yml up -d --build

echo "Website Re-deployed!"

#!/bin/bash

# cd into projects folder
cd /root/MLH-Portfolio

# git fetch
git fetch && git reset origin/main --hard

# enter python virtual environment
source python3-virtualenv/bin/activate

# install dependencies
pip install -r requirements.txt >/dev/null

# reload service and restart 'myportfolio' service
systemctl daemon-reload
systemctl restart myportfolio

echo "Website Re-deployed!"

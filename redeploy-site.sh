#!/bin/bash

# Kill all tmux sessions

tmux has-session -t "portfolio" 2>/dev/null
if [ $? != 1 ]; then tmux kill-server; fi

# cd into projects folder
cd /root/MLH-Portfolio

# git fetch
git fetch && git reset origin/main --hard

# enter python virtual environment
source python3-virtualenv/bin/activate

# install dependencies
pip install -r requirements.txt >/dev/null

# start new tmux session and start flask server
tmux new -s portfolio -d 'flask run --host=0.0.0.0'

echo "Website Re-deployed!"

#!/bin/bash

# Configuration
REPO_PATH=$(pwd)
PYTHON_SCRIPT="$REPO_PATH/auto_commit.py"
LOG_FILE="$REPO_PATH/bot_execution.log"

# Ask for user email if not provided
if [ -z "$GIT_EMAIL" ]; then
    echo "Please enter your GitHub email address (to attribute commits to your profile):"
    read GIT_EMAIL
fi

# Configure git
git config --global user.email "$GIT_EMAIL"
git config --global user.name "GitHub Contribution Bot"

# Make sure the Python script is executable
chmod +x "$PYTHON_SCRIPT"

# Add to crontab (runs every 4 hours at a random minute)
RANDOM_MINUTE=$(( ( RANDOM % 60 ) ))
CRON_JOB="$RANDOM_MINUTE */4 * * * /usr/bin/python3 $PYTHON_SCRIPT >> $LOG_FILE 2>&1"

# Check if the cron job already exists
(crontab -l 2>/dev/null | grep -F "$PYTHON_SCRIPT") || (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -

echo "Bot setup complete!"
echo "Commits will be made every 4 hours at minute $RANDOM_MINUTE."
echo "You can check the execution log at: $LOG_FILE"

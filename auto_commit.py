import os
import random
import subprocess
from datetime import datetime

# Configuration
REPO_PATH = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(REPO_PATH, "activity_log.txt")

# Realistic commit messages
COMMIT_MESSAGES = [
    "refactor: improve code structure",
    "docs: update README with new instructions",
    "fix: resolve minor bug in logging",
    "feat: add new utility function",
    "chore: update dependencies",
    "style: fix formatting issues",
    "perf: optimize performance in core module",
    "test: add unit tests for helper functions",
    "docs: fix typos in documentation",
    "build: update build script configuration"
]

def run_command(command):
    """Run a shell command and return the output."""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, cwd=REPO_PATH)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}\n{e.stderr}")
        return None

def make_commit():
    """Update a log file and make a git commit."""
    # 1. Update the log file
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"Activity logged at: {timestamp}\n")
    
    # 2. Git operations
    run_command("git add activity_log.txt")
    
    message = random.choice(COMMIT_MESSAGES)
    run_command(f'git commit -m "{message}"')
    
    # 3. Push to GitHub
    run_command("git push origin main")
    
    print(f"[{timestamp}] Successfully committed: {message}")

if __name__ == "__main__":
    # Ensure we are in the right directory
    os.chdir(REPO_PATH)
    make_commit()

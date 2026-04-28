# GitHub Contribution Bot

An automated tool designed to maintain a consistent GitHub contribution streak by periodically committing changes to a log file.

## Features

- **Automated Commits**: Automatically updates an activity log and pushes changes to GitHub.
- **Realistic Commit Messages**: Uses a variety of realistic commit messages to simulate natural development activity.
- **Scheduled Execution**: Includes a setup script to easily schedule the bot using `cron`.
- **Lightweight**: Minimal dependencies, using standard Python and Shell scripting.

## Getting Started

### Prerequisites

- Python 3.x
- Git
- GitHub CLI (`gh`) configured and authenticated

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CYBERTON00/github-contribution-bot.git
   cd github-contribution-bot
   ```

2. Run the setup script:
   ```bash
   chmod +x setup_bot.sh
   ./setup_bot.sh
   ```
   The script will prompt for your GitHub email and set up a cron job to run the bot every 4 hours.

## Files

- `auto_commit.py`: The core Python script that performs the commit and push operations.
- `setup_bot.sh`: Shell script for initial configuration and scheduling.
- `activity_log.txt`: The file modified by the bot to trigger commits.

## Disclaimer

This tool is for educational purposes. Use it responsibly and be aware that automated activity may be subject to GitHub's Terms of Service regarding bot activity.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

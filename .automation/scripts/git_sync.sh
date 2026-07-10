#!/bin/bash

# Exit immediately if any command exits with a non-zero status
set -e

# 1. Generate the formatted timestamp (YYYY-MM-DD HH:MM:SS)
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

# 2. Combine into your specific format string
COMMIT_MSG="vault backup: $TIMESTAMP"

# 3. Execute the Git workflow
echo "Staging all changes..."
git add -A

# Check if there are actually changes to commit to prevent errors
if git diff-index --quiet HEAD --; then
    echo "No changes detected. Skipping commit and push."
    exit 0
fi

echo "Committing changes with message: '$COMMIT_MSG'..."
git commit -m "$COMMIT_MSG"

echo "Pushing to remote repository..."
git push origin main

echo "✅ Backup successfully synced!"

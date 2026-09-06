#!/bin/bash

# Exit immediately if any command exits with a non-zero status
set -e

# 1. Generate the formatted timestamp (YYYY-MM-DD HH:MM:SS)
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

# 2. Combine into your specific format string
COMMIT_MSG="vault backup: $TIMESTAMP"

# 3. Ensure math blocks are normalized for Quartz before backup
VAULT_ROOT=$(cd "$(dirname "$0")/../.." && pwd)
SCRIPTS_DIR="$VAULT_ROOT/.automation/scripts"
VENV_PYTHON="$VAULT_ROOT/.automation/venv/bin/python3"

if [ -x "$VENV_PYTHON" ]; then
    "$VENV_PYTHON" "$SCRIPTS_DIR/fix_math_blocks.py" --quiet || true
elif command -v python3 >/dev/null 2>&1; then
    python3 "$SCRIPTS_DIR/fix_math_blocks.py" --quiet || true
fi

# 4. Execute the Git workflow
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

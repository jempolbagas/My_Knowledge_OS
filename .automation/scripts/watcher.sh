#!/bin/bash

# Find absolute paths relative to script location
VAULT_ROOT=$(cd "$(dirname "$0")/../.." && pwd)
SCRIPTS_DIR="$VAULT_ROOT/.automation/scripts"
VENV_PYTHON="$VAULT_ROOT/.automation/venv/bin/python3"

echo "Starting Knowledge OS File Watcher..."
echo "Vault Root: $VAULT_ROOT"

# Run initial indexing and validation on startup
echo "Running initial index and lint..."
$VENV_PYTHON "$SCRIPTS_DIR/build_index.py"
$VENV_PYTHON "$SCRIPTS_DIR/linter.py"
$VENV_PYTHON "$SCRIPTS_DIR/staleness_checker.py"
$VENV_PYTHON "$SCRIPTS_DIR/generate_summary.py"
echo "Initial validation completed."

# Monitor loop using inotifywait
# We monitor 20_Brain_Atlas, 10_Spaces, and 00_Inbox, excluding config/automation folders
inotifywait -m -r -e modify,create,delete,move --exclude "\.automation|\.obsidian|\.git|\.trash" \
  "$VAULT_ROOT/20_Brain_Atlas" "$VAULT_ROOT/10_Spaces" "$VAULT_ROOT/00_Inbox" 2>/dev/null | \
while true; do
    # Read the first event (blocks until a change occurs)
    read -r line || break
    
    # We detected a change! Enter a debounce loop.
    # We wait for a quiet period of 5 seconds (no new events).
    while read -t 5 -r next_line; do
        # Keep consuming events as long as they arrive within 5 seconds of each other
        true
    done
    
    # Quiet period of 5 seconds reached. Run the indexer and linter.
    echo "Change detected. Running automation scripts..."
    $VENV_PYTHON "$SCRIPTS_DIR/build_index.py"
    $VENV_PYTHON "$SCRIPTS_DIR/linter.py"
    $VENV_PYTHON "$SCRIPTS_DIR/staleness_checker.py"
    $VENV_PYTHON "$SCRIPTS_DIR/generate_summary.py"
    echo "Scripts execution finished. Watching for changes..."
done

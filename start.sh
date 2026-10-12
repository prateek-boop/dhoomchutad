#!/usr/bin/env bash
set -e

# EduEagle - Student Success & Intervention Orchestration Platform
# Startup script for Linux / macOS / Unix

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

PYTHON_BIN=""
for cmd in python3 python; do
    if command -v "$cmd" &>/dev/null; then
        PYTHON_BIN="$cmd"
        break
    fi
done

if [ -z "$PYTHON_BIN" ]; then
    echo "Error: Python 3 executable not found. Please ensure Python is installed." >&2
    exit 1
fi

echo "=========================================================="
echo "       EduEagle: Student Success & Intervention Engine    "
echo "=========================================================="
echo "Using Python runtime at: $($PYTHON_BIN --version) ($PYTHON_BIN)"

if [ ! -f "edueagle.db" ]; then
    echo "Initializing database & seeding realistic university cohort data..."
    "$PYTHON_BIN" database.py
fi

echo ""
echo "Launching web server on http://localhost:8000 ..."
echo "Press Ctrl+C to terminate the server anytime."
echo ""

exec "$PYTHON_BIN" server.py "$@"

#!/usr/bin/env bash
#
# uninstall.sh - Uninstall the GoombaStomp CLI (projectgoombastomp)
#
# This script removes the `goomba` executable, uninstalls the pip package,
# and cleans up the default output cache directory if present.
#
# Usage:
#   chmod +x uninstall.sh
#   ./uninstall.sh
#
set -e

echo "👉  Starting GoombaStomp CLI uninstall..."

# Remove executable if it exists in PATH
if command -v goomba >/dev/null 2>&1; then
    BIN_PATH=$(command -v goomba)
    echo "   • Removing executable at $BIN_PATH"
    sudo rm -f "$BIN_PATH"
else
    echo "   • No goomba executable found in PATH"
fi

# Uninstall pip package
echo "   • Uninstalling Python package (requires pip)"
pip uninstall -y projectgoombastomp || true

# Remove cache/output directory if the default exists
DEFAULT_CACHE_DIR="$HOME/.goombastomp"
if [ -d "$DEFAULT_CACHE_DIR" ]; then
    echo "   • Removing cache directory $DEFAULT_CACHE_DIR"
    rm -rf "$DEFAULT_CACHE_DIR"
fi

echo "✅  GoombaStomp CLI successfully uninstalled!"

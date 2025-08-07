#!/usr/bin/env bash
#
# 🗑️ ProjectGoombaStomp Uninstaller
#
# Removes the ProjectGoombaStomp CLI cleanly from your system
#
set -e

echo "🗑️ Uninstalling ProjectGoombaStomp CLI..."

# Use pip3 if available, otherwise pip
PIP_CMD="pip3"
if ! command -v pip3 >/dev/null 2>&1; then
    PIP_CMD="pip"
fi

# Uninstall the Python package
echo "📦 Removing Python package..."
$PIP_CMD uninstall -y projectgoombastomp 2>/dev/null || echo "   Package not found (already removed?)"

# Remove goomba command if it exists in PATH
if command -v goomba >/dev/null 2>&1; then
    GOOMBA_PATH=$(command -v goomba)
    echo "🔍 Found goomba at: $GOOMBA_PATH"
    
    # Only remove if it's in user space (safer)
    if [[ "$GOOMBA_PATH" == *"$HOME"* ]]; then
        echo "🗑️ Removing goomba executable..."
        rm -f "$GOOMBA_PATH"
    else
        echo "⚠️  goomba found at system location: $GOOMBA_PATH"
        echo "   You may need to remove it manually with: sudo rm $GOOMBA_PATH"
    fi
fi

# Clean up cache directories if they exist
CACHE_DIRS=(
    "$HOME/.goombastomp"
    "$HOME/.cache/goombastomp"
    "$HOME/.local/share/goombastomp"
)

for cache_dir in "${CACHE_DIRS[@]}"; do
    if [ -d "$cache_dir" ]; then
        echo "🧹 Removing cache directory: $cache_dir"
        rm -rf "$cache_dir"
    fi
done

echo ""
echo "✅ ProjectGoombaStomp CLI has been successfully uninstalled!"
echo "💡 Note: PATH modifications in your shell config files were not automatically removed."
echo "   You can manually clean up entries in ~/.bashrc, ~/.zshrc, etc. if desired."

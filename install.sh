#!/usr/bin/env bash
#
# 🚀 ProjectGoombaStomp Easy Installer
# 
# This script makes installation painless for everyone, including non-technical users.
# It automatically handles Python package installation and ensures the 'goomba' command works.
#
set -e

echo "🚀 Installing ProjectGoombaStomp CLI..."
echo ""

# Check if Python is available
if ! command -v python3 >/dev/null 2>&1; then
    echo "❌ Python 3 is required but not found."
    echo "💡 Please install Python 3 from https://python.org and try again."
    exit 1
fi

# Check if pip is available
if ! command -v pip3 >/dev/null 2>&1 && ! command -v pip >/dev/null 2>&1; then
    echo "❌ pip is required but not found."
    echo "💡 Please install pip and try again."
    exit 1
fi

# Use pip3 if available, otherwise pip
PIP_CMD="pip3"
if ! command -v pip3 >/dev/null 2>&1; then
    PIP_CMD="pip"
fi

echo "✅ Found Python and pip"

# Install the package
echo "📦 Installing ProjectGoombaStomp package..."
$PIP_CMD install --user --upgrade .

# Get the user bin directory
USER_BIN=$(python3 -c "import site, os; print(os.path.join(site.getuserbase(), 'bin'))" 2>/dev/null || echo "$HOME/.local/bin")

echo "🔍 Looking for goomba executable..."

# Check if goomba is already in PATH
if command -v goomba >/dev/null 2>&1; then
    echo "✅ goomba command is ready to use!"
    echo ""
    echo "🎉 Installation complete!"
    echo "📚 Try it out: goomba --help"
    exit 0
fi

# Check if goomba exists in user bin
if [ -f "$USER_BIN/goomba" ]; then
    echo "📂 Found goomba at: $USER_BIN/goomba"
    
    # Check if user bin is in PATH
    if [[ ":$PATH:" != *":$USER_BIN:"* ]]; then
        echo "🔧 Adding $USER_BIN to your PATH..."
        
        # Detect shell and update appropriate config file
        SHELL_NAME=$(basename "${SHELL:-bash}")
        case $SHELL_NAME in
            zsh)
                RC_FILE="$HOME/.zshrc"
                ;;
            bash)
                RC_FILE="$HOME/.bashrc"
                [ -f "$HOME/.bash_profile" ] && RC_FILE="$HOME/.bash_profile"
                ;;
            fish)
                RC_FILE="$HOME/.config/fish/config.fish"
                mkdir -p "$(dirname "$RC_FILE")"
                ;;
            *)
                RC_FILE="$HOME/.profile"
                ;;
        esac
        
        # Add PATH export to shell config
        echo "" >> "$RC_FILE"
        echo "# Added by ProjectGoombaStomp installer" >> "$RC_FILE"
        if [ "$SHELL_NAME" = "fish" ]; then
            echo "set -gx PATH $USER_BIN \$PATH" >> "$RC_FILE"
        else
            echo "export PATH=\"$USER_BIN:\$PATH\"" >> "$RC_FILE"
        fi
        
        echo "✅ Updated $RC_FILE"
        echo "🔄 Reloading shell configuration..."
        
        # Try to source the config file
        if [ "$SHELL_NAME" != "fish" ]; then
            # shellcheck source=/dev/null
            source "$RC_FILE" 2>/dev/null || true
        fi
        
        # Update PATH for current session
        export PATH="$USER_BIN:$PATH"
    fi
    
    # Final check
    if command -v goomba >/dev/null 2>&1; then
        echo "✅ goomba command is ready to use!"
    else
        echo "⚠️  Installation complete, but you may need to restart your terminal"
        echo "   or run: export PATH=\"$USER_BIN:\$PATH\""
    fi
    
else
    echo "❌ goomba executable not found after installation."
    echo "💡 This might be a Python environment issue."
    echo "   Try: $PIP_CMD install --user --force-reinstall ."
    exit 1
fi

echo ""
echo "🎉 Installation complete!"
echo "📚 Get started with: goomba --help"
echo "📁 Example usage: goomba ./my_project --pdf --zip"

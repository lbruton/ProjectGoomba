    #!/usr/bin/env bash
    #
    # install.sh - idiot‑proof installer for GoombaStomp CLI
    #
    # • Installs the Python package in --user space
    # • Symlinks the launcher to ~/.local/bin/goomba
    # • Adds ~/.local/bin to PATH in your shell's startup file if missing
    # • Refreshes the current shell so 'goomba' works immediately
    #
    set -euo pipefail

    echo "👉 Installing GoombaStomp CLI..."

    pip install --upgrade --user .

    USER_BIN=$(python3 - <<'PY'
import site, os
print(os.path.join(site.getuserbase(), "bin"))
PY
    )

    LAUNCHER="$USER_BIN/goomba"
    if [ ! -x "$LAUNCHER" ]; then
        echo "❌ goomba script not found in $USER_BIN"
        exit 1
    fi

    mkdir -p "$HOME/.local/bin"
    ln -sf "$LAUNCHER" "$HOME/.local/bin/goomba"
    echo "   • Symlinked $LAUNCHER → $HOME/.local/bin/goomba"

    # Ensure ~/.local/bin on PATH
    if ! echo ":$PATH:" | grep -q ":$HOME/.local/bin:"; then
        echo "   • Adding ~/.local/bin to PATH"
        SHELL_NAME=$(basename "${SHELL:-sh}")

        if [ "$SHELL_NAME" = "zsh" ]; then
            RC="$HOME/.zprofile"
        elif [ "$SHELL_NAME" = "bash" ]; then
            RC="$HOME/.bash_profile"
            [ -f "$RC" ] || RC="$HOME/.bashrc"
        else
            RC="$HOME/.profile"
        fi

        echo -e "\n# Added by GoombaStomp installer\nexport PATH=\"$HOME/.local/bin:$PATH\"" >> "$RC"
        # shellcheck source=/dev/null
        source "$RC"
        echo "   • Updated $RC"
    fi

    hash -r
    echo "✅ Installation complete. Run 'goomba --help' to get started."

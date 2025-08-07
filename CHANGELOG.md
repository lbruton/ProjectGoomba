# Changelog
## [1.0.5] - 2025-08-07

### Fixed
- **install.sh** is now self‑healing: it appends `~/.local/bin` to your shell’s startup file
  (`.zprofile`, `.bash_profile`, etc.) if it’s missing, sources the file, and refreshes the shell
  so the `goomba` command works immediately after install.

### Changed
- Bumped version to `1.0.5` in `setup.py`.

## [1.0.4] - 2025-08-07

### Added
- Comprehensive **README.md** with installation, usage, examples, and troubleshooting.
- Expanded **LLM.md** prompt guide.

### Changed
- Documentation only – no functional code changes.

## [1.0.3] - 2025-08-07

### Fixed
- **install.sh** now detects pip’s user-bin directory and symlinks `goomba` into `~/.local/bin`, so the command works out of the box on macOS/Homebrew and other setups where `pip --user` scripts are placed outside your PATH.

### Changed
- Bumped version to `1.0.3` in `setup.py`.

## [1.0.2] - 2025-08-07

### Added
- **install.sh** script installs the package in user space (`~/.local`) and guarantees the launcher is at `~/.local/bin/goomba`.

### Changed
- Bumped version to `1.0.2` in `setup.py`.

## [1.0.1] - 2025-08-06

### Added
- **Uninstall script:** `uninstall.sh` for straightforward removal of the CLI and its artifacts.

### Changed
- Bumped package version to `1.0.1` in `setup.py`.



## [1.0.0] - Initial Release

### Added
- Command-line tool: `goombastomp`
- Recursively scans a target folder and builds:
  - Folder structure tree
  - Consolidated content from all text/code files
- Generates output in Markdown (`.md`) format
- Optional PDF export with UTF-8 (Unicode) support via `fpdf2`
- Optional ZIP archive containing all outputs
- Outputs are placed inside a `merged/` subfolder in the scanned directory
- Support for common text and config files: `.txt`, `.md`, `.log`, `.json`, `.yaml`, `.csv`, `.ini`, etc.
- Optional code file inclusion: `.py`, `.js`, `.html`, `.css`
- Clean, pip-installable package with `goombastomp` as CLI entry point
- Added `LLM.md` with a prompt to resume work or extend the project

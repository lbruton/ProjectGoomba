# 📁 ProjectGoombaStomp CLI (`goomba`)

> **One-command directory documentation** – Turn any folder into beautiful Markdown docs with optional PDF and ZIP exports.

ProjectGoombaStomp is perfect for code reviews, project handoffs, compliance documentation, or just understanding what's in that folder you forgot about. Point it at any directory and get instant, comprehensive documentation.

## ✨ What it does

- 📂 **Scans directories** and creates a visual folder tree
- 📝 **Extracts file contents** from text files, configs, and optionally source code
- 🎨 **Generates beautiful Markdown** with syntax highlighting  
- 📄 **Exports to PDF** for sharing and archiving
- 📦 **Bundles everything in ZIP** for easy distribution
- 🚀 **Works anywhere** – no complex setup required

## 🚀 Quick Start

### One-Line Installation

```bash
# Download and extract the project, then run:
chmod +x install.sh && ./install.sh
```

That's it! The installer handles everything automatically, including adding `goomba` to your PATH.

### Basic Usage

```bash
# Document a project folder
goomba ./my_project

# Include source code files too  
goomba ./my_project --include-code

# Create PDF and ZIP bundles
goomba ./my_project --pdf --zip

# Generate everything at once
goomba ./my_project --all
```

## 📋 Examples

### Document a Python project
```bash
goomba ./my_python_app --include-code --pdf
```
Creates:
- `merged/merged_output.md` - Complete Markdown documentation
- `merged/merged_output.pdf` - PDF version for sharing

### Audit a configuration directory
```bash
goomba /etc/myapp --zip
```
Perfect for compliance documentation and configuration audits.

### Create project handoff package
```bash
goomba ./legacy_project --all
```
Generates Markdown, PDF, and ZIP with all source code included.

## 🎯 Command Options

| Option | Description |
|--------|-------------|
| `--include-code` | Include source code files (`.py`, `.js`, `.html`, etc.) |
| `--pdf` | Generate PDF version (requires `fpdf2`) |
| `--zip` | Bundle all outputs in a ZIP file |
| `--all` | Enable all options above |
| `--help` | Show detailed help |
| `--version` | Show version information |

## 📁 What Files Are Included?

### Always Included
- Text files: `.txt`, `.md`, `.rst`, `.log`
- Config files: `.json`, `.yaml`, `.ini`, `.toml`, `.cfg`
- Data files: `.csv`, `.xml`

### With `--include-code`
- Python: `.py`
- JavaScript/TypeScript: `.js`, `.ts`  
- Web: `.html`, `.css`, `.scss`
- Other: `.php`, `.rb`, `.go`, `.java`, `.c`, `.cpp`, `.cs`
- Scripts: `.sh`, `.bat`, `.ps1`
- And many more!

## 🔧 Installation Methods

### Method 1: Easy Installer (Recommended)
```bash
# Extract the project and run
chmod +x install.sh
./install.sh
```

### Method 2: Manual pip install
```bash
pip install --user .
# Then add ~/.local/bin to your PATH manually
```

### Method 3: Development install
```bash
git clone https://github.com/yourhandle/ProjectGoombaStomp.git
cd ProjectGoombaStomp
pip install --user -e .
```

## 🗑️ Uninstallation

```bash
chmod +x uninstall.sh
./uninstall.sh
```

Removes the package, command, and any cache directories cleanly.

## 💡 Pro Tips

- **Large projects**: The tool automatically skips files larger than 1MB and limits directory depth
- **Sensitive data**: Review the generated docs before sharing – they contain actual file contents
- **PDF fonts**: Uses system fonts for maximum compatibility
- **Output location**: Everything goes into a `merged/` folder in your target directory

## 🛠️ Requirements

- **Python 3.7+** (comes with most modern systems)
- **pip** for installation
- **fpdf2** for PDF generation (installed automatically)

## 🐛 Troubleshooting

### "goomba command not found"
```bash
# Try restarting your terminal, or manually add to PATH:
export PATH="$HOME/.local/bin:$PATH"
```

### PDF generation fails
```bash
# Install fpdf2 manually:
pip install --user fpdf2
```

### Permission errors
```bash
# Make sure you can read the target directory:
ls -la /path/to/directory
```

## 📊 Example Output Structure

```
my_project/
├── merged/
│   ├── merged_output.md      # 📝 Markdown documentation
│   ├── merged_output.pdf     # 📄 PDF version (if --pdf)
│   └── merged_output.zip     # 📦 ZIP bundle (if --zip)
├── src/
├── docs/
└── README.md
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test them
4. Submit a pull request

## 📄 License

MIT License - feel free to use this in your projects!

## 🙋‍♂️ Support

- 📖 **Documentation**: This README covers most use cases
- 🐛 **Bug Reports**: Open an issue on GitHub
- 💡 **Feature Requests**: We'd love to hear your ideas!

---

**Made with ❤️ by developers, for developers**

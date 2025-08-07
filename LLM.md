# LLM.md – Development Guide for ProjectGoombaStomp v1.0

This file helps AI assistants and developers quickly understand the ProjectGoombaStomp codebase and continue development.

## 🎯 Project Overview

**ProjectGoombaStomp** is a command-line tool (`goomba`) that transforms directories into comprehensive documentation:

- **Input**: Any directory/folder
- **Output**: Markdown files with optional PDF and ZIP exports
- **Purpose**: Code reviews, project handoffs, compliance docs, directory auditing

## 🏗️ Architecture

### Core Components

```
ProjectGoomba/
├── projectgoombastomp/      # Main package
│   ├── __init__.py         # Package metadata and version info
│   ├── cli.py             # Main CLI application logic
│   └── fpdf_fonts/        # (Legacy - should be removed)
├── setup.py               # Package configuration and dependencies
├── install.sh             # User-friendly installer script
├── uninstall.sh           # Clean removal script
├── README.md              # Comprehensive user documentation
├── CHANGELOG.md           # Version history and release notes
└── LLM.md                 # This developer guide
```

### Key Functions in `cli.py`

1. **`build_folder_structure()`** - Generates ASCII tree view of directories
2. **`collect_file_contents()`** - Extracts and formats file contents
3. **`generate_markdown()`** - Combines structure + content into Markdown
4. **`save_pdf()`** - Exports to PDF using fpdf2 with system fonts
5. **`save_zip()`** - Bundles outputs into ZIP archives

### File Type Support

- **Always included**: `.txt`, `.md`, `.log`, `.json`, `.yaml`, `.ini`, `.csv`, `.xml`
- **Code files** (with `--include-code`): `.py`, `.js`, `.html`, `.css`, `.php`, `.rb`, `.go`, etc.
- **Excluded**: Hidden files, `node_modules`, `.git`, large files >1MB

## 🔧 Development Context

### Version 1.0 Improvements Made

1. **Fixed PDF Generation**: Removed problematic bundled font dependencies, now uses system fonts
2. **Enhanced Error Handling**: Comprehensive error handling for file access, permissions, encoding
3. **Improved Installation**: Smart installer that handles PATH configuration automatically
4. **Code Cleanup**: More modular, readable code with better documentation
5. **Better CLI UX**: Clearer help text, examples, and progress indicators

### Technology Stack

- **Python 3.7+** - Core language (supports older Python versions)
- **fpdf2** - PDF generation library (system font approach for compatibility)
- **argparse** - Command-line interface
- **pathlib/os** - File system operations
- **zipfile** - Archive creation

### Key Design Decisions

- **System fonts over bundled fonts** - Better compatibility, fewer dependencies
- **User-space installation** - Avoids sudo requirements, cleaner for end users
- **Progressive enhancement** - Base Markdown always works, PDF/ZIP are optional
- **Safety-first** - File size limits, depth limits, permission checks

## 🚀 Common Development Tasks

### Adding New File Types

```python
# In cli.py, extend the extension sets:
code_extensions = {
    ".py", ".js", # ... existing types
    ".new_extension",  # Add new type here
}
```

### Improving PDF Output

```python
# In save_pdf() function:
# - Adjust font sizes for different markdown elements
# - Add better line wrapping logic
# - Handle special characters or symbols
```

### Enhanced Error Handling

```python
# Common patterns used:
try:
    # risky operation
except (PermissionError, OSError) as e:
    print(f"❌ Error: {e}")
    # graceful fallback or exit
```

## 🎯 Future Enhancement Ideas

### High Priority
- **Configuration file support** - Allow users to customize file extensions, exclusions
- **Better PDF styling** - Headers, TOC, page numbers, better code formatting
- **Progress indicators** - Show progress for large directory scans
- **Include/exclude patterns** - Allow glob patterns for fine-grained control

### Medium Priority
- **HTML export** - Alternative to PDF with better styling options
- **Template system** - Allow custom Markdown templates
- **Plugin architecture** - Support for custom file processors
- **Multi-format support** - DOCX, RTF export options

### Low Priority
- **GUI version** - Desktop application for non-technical users
- **Cloud integration** - Direct upload to GitHub, Google Drive, etc.
- **Diff mode** - Compare two directories and show changes
- **Database support** - Index and search historical scans

## 🔍 Code Quality Standards

- **Type hints** - Use for function parameters and returns
- **Error handling** - Always handle file operations gracefully
- **User feedback** - Provide clear success/error messages with emojis
- **Cross-platform** - Test on macOS, Linux, Windows
- **Python 3.7+ compatibility** - Don't use newer language features

## 💡 LLM Prompt Template

When working on this project, use this context:

```
You're working on ProjectGoombaStomp v1.0, a Python CLI tool that documents directories.

Key facts:
- Command name: "goomba"
- Current version: 1.0 (fresh start)
- Main file: projectgoombastomp/cli.py
- Uses fpdf2 for PDF generation with system fonts
- Target: Python 3.7+ compatibility
- Focus: User-friendly installation and robust error handling

Recent improvements: Fixed PDF font issues, enhanced installer, better error handling.

Please maintain the existing code style and ensure any changes are backwards compatible.
```

## 📚 Useful References

- [fpdf2 Documentation](https://py-pdf.github.io/fpdf2/) - PDF generation
- [argparse Tutorial](https://docs.python.org/3/tutorial/stdlib2.html#command-line-arguments) - CLI design
- [setuptools Guide](https://setuptools.pypa.io/en/latest/userguide/) - Python packaging
- [pathlib Documentation](https://docs.python.org/3/library/pathlib.html) - Modern file handling

## 🗑️ Cleanup Notes

The `projectgoombastomp/fpdf_fonts/` directory should be removed as it's no longer needed. The new implementation uses system fonts instead of bundled fonts for better compatibility.

---

*This guide ensures consistent development and helps maintain the project's quality and user experience.*

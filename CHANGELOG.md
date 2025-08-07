# Changelog

All notable changes to ProjectGoombaStomp will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-08-06

### 🎉 Initial Stable Release

ProjectGoombaStomp CLI is ready for prime time! This stable release provides reliable directory documentation with multiple export formats.

#### ✨ Features
- **Directory Scanning**: Recursively scan folders and generate visual tree structures
- **Content Extraction**: Extract and format contents from text files, configs, and source code
- **Markdown Export**: Generate clean, well-formatted Markdown documentation with syntax highlighting
- **PDF Export**: Create professional PDF documents using system fonts for maximum compatibility
- **ZIP Bundling**: Package all outputs into convenient ZIP archives
- **Smart File Detection**: Automatically includes appropriate file types based on extensions
- **Code Support**: Optional inclusion of source code files with `--include-code` flag
- **Safety Features**: 
  - Automatic file size limits (1MB max per file)
  - Directory depth limiting to prevent infinite loops
  - Permission error handling
  - Unicode-safe text processing

#### 🛠️ Technical Improvements
- **Robust PDF Generation**: Fixed font handling issues by using system fonts instead of bundled fonts
- **Better Error Handling**: Comprehensive error handling for file access, encoding, and permission issues
- **Enhanced CLI**: More user-friendly command-line interface with better help text and examples
- **Improved Installation**: Pain-free installer that automatically handles PATH configuration
- **Cross-Platform**: Works on macOS, Linux, and Windows with Python 3.7+

#### 📦 Installation & Usage
- **Simple Installation**: One-command installer handles everything automatically
- **Clean Uninstallation**: Complete removal script for easy cleanup
- **Comprehensive Documentation**: Detailed README with examples and troubleshooting

#### 🔧 Dependencies
- Python 3.7+ (required)
- fpdf2 >=2.5.0 (for PDF generation)

#### 📝 Command Options
- `goomba <directory>` - Basic Markdown documentation
- `--include-code` - Include source code files
- `--pdf` - Generate PDF version
- `--zip` - Create ZIP bundle
- `--all` - Enable all options

---

## Development Notes

This release represents a complete rewrite and cleanup of the original codebase, focusing on:

1. **Reliability**: Robust error handling and fallback mechanisms
2. **Usability**: Simplified installation and clearer documentation
3. **Maintainability**: Clean, well-documented code structure
4. **Compatibility**: Works across different Python versions and operating systems

The PDF generation issue from previous versions has been completely resolved by switching to system fonts and improving the text rendering pipeline.

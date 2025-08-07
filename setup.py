"""
ProjectGoombaStomp setup configuration
"""
from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

setup(
    name="projectgoombastomp",
    version="1.0",
    author="Lonnie",
    author_email="",
    description="Command-line tool to document directories as Markdown, PDF, or ZIP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourhandle/ProjectGoombaStomp",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
        "Topic :: System :: Archiving",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Console Application",
    ],
    keywords="documentation markdown pdf cli directory scanner",
    python_requires=">=3.7",
    install_requires=[
        "fpdf2>=2.5.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
        ],
    },
    entry_points={
        "console_scripts": [
            "goomba=projectgoombastomp.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)

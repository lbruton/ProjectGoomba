# ProjectGoombaStomp Development Makefile
# 
# Common development tasks made easy

.PHONY: help install uninstall test clean dev-install format lint

help:
	@echo "🚀 ProjectGoombaStomp Development Commands"
	@echo ""
	@echo "  make install     - Install the package locally"
	@echo "  make uninstall   - Remove the package"
	@echo "  make dev-install - Install in development mode"
	@echo "  make test        - Run the test suite"
	@echo "  make format      - Format code with black"
	@echo "  make lint        - Lint code with flake8"
	@echo "  make clean       - Clean up build artifacts"
	@echo ""

install:
	@echo "📦 Installing ProjectGoombaStomp..."
	chmod +x install.sh
	./install.sh

uninstall:
	@echo "🗑️ Uninstalling ProjectGoombaStomp..."
	chmod +x uninstall.sh
	./uninstall.sh

dev-install:
	@echo "🔧 Installing in development mode..."
	pip install --user -e .

test:
	@echo "🧪 Running tests..."
	python -m pytest tests/ -v

format:
	@echo "🎨 Formatting code..."
	python -m black projectgoombastomp/ tests/

lint:
	@echo "🔍 Linting code..."
	python -m flake8 projectgoombastomp/ tests/

clean:
	@echo "🧹 Cleaning up..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

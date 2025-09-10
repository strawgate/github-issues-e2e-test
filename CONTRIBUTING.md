# Contributing to G.I.T.H.U.B. - The Existential Code Companion

*"Every contribution is a step on the path of digital enlightenment. Welcome, fellow seeker of code wisdom."*

Thank you for your interest in contributing to G.I.T.H.U.B.! This document provides guidelines for those brave souls who wish to join us on this journey of existential coding.

## Getting Started

### Prerequisites
- Python 3.13 or higher
- UV package manager
- Git

### Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/github-issues-e2e-test.git
   cd github-issues-e2e-test
   ```

3. Install dependencies:
   ```bash
   uv sync
   ```

4. Install development dependencies:
   ```bash
   uv add --dev pytest black isort mypy
   ```

## Development Workflow

### Branch Naming
- `feature/description` - New features
- `bugfix/description` - Bug fixes
- `hotfix/description` - Critical fixes
- `docs/description` - Documentation updates

### Commit Messages
Follow conventional commits format:
- `feat: add new feature`
- `fix: resolve bug in module`
- `docs: update README`
- `test: add unit tests for feature`

### Code Style

We use the following tools for code quality:
- **Black** for code formatting
- **isort** for import sorting
- **mypy** for type checking
- **pytest** for testing

Run all checks before committing:
```bash
black .
isort .
mypy .
pytest
```

## Pull Request Process

1. Create a feature branch from `main`
2. Make your changes
3. Add tests for new functionality
4. Update documentation if needed
5. Run all tests and linting
6. Submit a pull request

### PR Template
- Clear description of changes
- Reference related issues
- Screenshots for UI changes
- Breaking changes clearly marked

## Issue Reporting

When reporting issues, please include:
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages/logs

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Follow the golden rule

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- Project documentation

## Questions?

Feel free to open an issue or start a discussion for any questions about contributing.

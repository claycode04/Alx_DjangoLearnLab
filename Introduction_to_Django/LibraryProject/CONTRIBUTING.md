# Contributing to Django Library Project

Thank you for your interest in contributing to the Django Library Project! This document provides guidelines and instructions for contributing.

## 🚀 Quick Start

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/Alx_DjangoLearnLab.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate it: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/Mac)
5. Install dependencies: `pip install -r requirements.txt`
6. Create a new branch: `git checkout -b feature/your-feature-name`

## 📋 Development Guidelines

### Code Style
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused
- Use type hints where appropriate

### Django Best Practices
- Use Django's built-in features whenever possible
- Follow the DRY (Don't Repeat Yourself) principle
- Use Django's ORM instead of raw SQL
- Implement proper error handling
- Use Django's security features

### Git Workflow
1. Always create a new branch for your feature
2. Use descriptive commit messages
3. Keep commits small and focused
4. Rebase your branch before submitting a PR

### Commit Message Format
```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

Examples:
- `feat(books): add book search functionality`
- `fix(auth): resolve login redirect issue`
- `docs(readme): update installation instructions`

## 🧪 Testing

### Running Tests
```bash
python manage.py test
```

### Writing Tests
- Write tests for all new features
- Include both positive and negative test cases
- Test edge cases and error conditions
- Use Django's TestCase class
- Mock external dependencies

### Test Structure
```python
from django.test import TestCase
from django.contrib.auth.models import User

class BookModelTest(TestCase):
    def setUp(self):
        """Set up test data"""
        pass
    
    def test_book_creation(self):
        """Test book creation"""
        pass
    
    def tearDown(self):
        """Clean up after tests"""
        pass
```

## 📝 Documentation

- Update README.md for significant changes
- Add docstrings to new functions and classes
- Update CHANGELOG.md
- Include code examples in documentation

## 🐛 Bug Reports

When reporting bugs, please include:
- Django version
- Python version
- Operating system
- Steps to reproduce
- Expected behavior
- Actual behavior
- Error messages (if any)

## 💡 Feature Requests

When requesting features:
- Describe the use case
- Explain why it's needed
- Provide examples of how it would work
- Consider backwards compatibility

## 🔍 Code Review Process

1. All changes must be reviewed before merging
2. Ensure all tests pass
3. Check for code style compliance
4. Verify documentation is updated
5. Test the feature manually

## 📚 Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Python PEP 8](https://www.python.org/dev/peps/pep-0008/)
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)

## 📞 Getting Help

- Create an issue for bugs or questions
- Join our community discussions
- Check existing issues before creating new ones

## 🙏 Recognition

Contributors will be recognized in:
- README.md contributors section
- CHANGELOG.md for their contributions
- GitHub contributors page

Thank you for contributing to making this project better! 🎉

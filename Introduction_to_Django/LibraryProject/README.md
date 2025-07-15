# 📚 Django Library Management System

A modern, efficient library management system built with Django 5.2.4. This project demonstrates best practices in Django development with clean architecture and fast performance.

## 🚀 Features

- **Book Management**: Add, edit, delete, and search books
- **User Authentication**: Secure login/logout system
- **Book Borrowing**: Track book loans and returns
- **Admin Interface**: Powerful Django admin for management with custom configurations
- **Advanced Search**: Search books by title, author, or ISBN
- **Smart Filtering**: Filter by publication year, cover type, and language
- **Bulk Actions**: Perform bulk operations on multiple books
- **Responsive Design**: Mobile-friendly interface
- **Fast Search**: Optimized database queries
- **Clean Code**: Following Django best practices

## 📋 Quick Start

### Prerequisites
- Python 3.8+
- Django 5.2.4
- SQLite (default) or PostgreSQL

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/claycode04/Alx_DjangoLearnLab.git
   cd LibraryProject
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000` to see your application!

## 🏗️ Project Structure

```
LibraryProject/
├── manage.py              # Django management script
├── db.sqlite3            # SQLite database
├── README.md             # Project documentation
└── LibraryProject/       # Main project directory
    ├── __init__.py
    ├── settings.py       # Project settings
    ├── urls.py          # URL routing
    ├── wsgi.py          # WSGI configuration
    └── asgi.py          # ASGI configuration
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file for production:
```env
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### Database Setup
The project uses SQLite by default. For production, consider PostgreSQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'library_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 📊 Performance Features

- **Optimized Queries**: Using `select_related()` and `prefetch_related()`
- **Database Indexing**: Strategic indexes on frequently queried fields
- **Caching**: Redis support for session and query caching
- **Compression**: Static file compression for faster loading

## 🛡️ Security Features

- **CSRF Protection**: Built-in Django CSRF protection
- **SQL Injection Prevention**: Django ORM prevents SQL injection
- **XSS Protection**: Template auto-escaping
- **Secure Headers**: Security middleware configuration

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

For coverage reports:
```bash
pip install coverage
coverage run manage.py test
coverage report
```

## 📱 API Endpoints (Future)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/books/` | List all books |
| POST | `/api/books/` | Create new book |
| GET | `/api/books/{id}/` | Get book details |
| PUT | `/api/books/{id}/` | Update book |
| DELETE | `/api/books/{id}/` | Delete book |

## 🎨 UI/UX Features

- **Bootstrap 5**: Modern, responsive design
- **Clean Interface**: Intuitive user experience
- **Fast Loading**: Optimized assets and minimal JavaScript
- **Accessibility**: WCAG 2.1 compliant

## 🚀 Deployment

### Heroku Deployment
```bash
pip install gunicorn
pip freeze > requirements.txt
# Configure Procfile and runtime.txt
git add .
git commit -m "Prepare for deployment"
heroku create your-app-name
git push heroku main
```

### Docker Deployment
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Framework
- ALX Software Engineering Program
- OFPPT Educational Institution

## 📞 Support

For support, email: your-email@example.com or create an issue on GitHub.

---

**Made with ❤️ using Django**
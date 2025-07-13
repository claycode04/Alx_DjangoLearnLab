# Django Library Project - Deployment Guide

## Overview
This guide covers various deployment options for the Django Library Management System.

## 🚀 Production Deployment

### Prerequisites
- Python 3.8+
- PostgreSQL 12+
- Redis (for caching)
- Nginx (for reverse proxy)

### Environment Setup

1. **Create production environment file**
   ```bash
   cp .env.example .env
   ```

2. **Update environment variables**
   ```env
   DEBUG=False
   SECRET_KEY=your-super-secret-production-key
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   DATABASE_URL=postgresql://user:password@localhost:5432/library_db
   CACHE_URL=redis://localhost:6379/1
   ```

### Database Setup

1. **Create PostgreSQL database**
   ```sql
   CREATE DATABASE library_db;
   CREATE USER library_user WITH PASSWORD 'secure_password';
   GRANT ALL PRIVILEGES ON DATABASE library_db TO library_user;
   ```

2. **Run migrations**
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```

## 🐳 Docker Deployment

### Development with Docker
```bash
docker-compose up --build
```

### Production with Docker
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Docker Environment Variables
```env
DJANGO_SETTINGS_MODULE=LibraryProject.settings.production
DATABASE_URL=postgresql://postgres:postgres@db:5432/library_db
REDIS_URL=redis://redis:6379/1
```

## ☁️ Cloud Deployment

### Heroku Deployment

1. **Install Heroku CLI**
   ```bash
   heroku login
   ```

2. **Create Heroku app**
   ```bash
   heroku create your-library-app
   ```

3. **Add PostgreSQL addon**
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

4. **Add Redis addon**
   ```bash
   heroku addons:create heroku-redis:hobby-dev
   ```

5. **Set environment variables**
   ```bash
   heroku config:set DEBUG=False
   heroku config:set SECRET_KEY=your-secret-key
   ```

6. **Deploy**
   ```bash
   git push heroku main
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

### AWS Deployment (EC2 + RDS)

1. **Launch EC2 instance**
   - Choose Ubuntu 20.04 LTS
   - Configure security groups (80, 443, 22)

2. **Install dependencies**
   ```bash
   sudo apt update
   sudo apt install python3-pip nginx postgresql-client redis-server
   pip3 install -r requirements.txt
   ```

3. **Setup RDS PostgreSQL**
   - Create RDS instance
   - Configure security groups
   - Update DATABASE_URL

4. **Configure Nginx**
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
       
       location /static/ {
           alias /path/to/staticfiles/;
       }
       
       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

### DigitalOcean App Platform

1. **Create app.yaml**
   ```yaml
   name: library-project
   services:
   - name: web
     source_dir: /
     github:
       repo: your-username/your-repo
       branch: main
     run_command: gunicorn LibraryProject.wsgi
     environment_slug: python
     instance_count: 1
     instance_size_slug: basic-xxs
     env:
     - key: DEBUG
       value: "False"
     - key: SECRET_KEY
       value: "your-secret-key"
   databases:
   - name: library-db
     engine: PG
     version: "12"
   ```

## 🔧 Performance Optimization

### Database Optimization
```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'library_db',
        'USER': 'library_user',
        'PASSWORD': 'secure_password',
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {
            'MAX_CONNS': 20,
            'CONN_MAX_AGE': 60,
        }
    }
}
```

### Redis Caching
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

### Static Files with CDN
```python
# For AWS S3
AWS_ACCESS_KEY_ID = 'your-access-key'
AWS_SECRET_ACCESS_KEY = 'your-secret-key'
AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
AWS_S3_REGION_NAME = 'us-west-2'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```

## 🔒 Security Checklist

### Production Security
- [ ] Set DEBUG=False
- [ ] Use strong SECRET_KEY
- [ ] Configure ALLOWED_HOSTS
- [ ] Enable HTTPS/SSL
- [ ] Set secure cookies
- [ ] Configure CORS properly
- [ ] Use environment variables for secrets
- [ ] Regular security updates
- [ ] Database connection encryption
- [ ] Firewall configuration

### SSL/HTTPS Setup
```bash
# Using Let's Encrypt with Certbot
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

## 📊 Monitoring and Logging

### Application Monitoring
```python
# Install Sentry for error tracking
pip install sentry-sdk[django]

# settings.py
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="your-sentry-dsn",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
)
```

### Health Checks
```python
# views.py
from django.http import JsonResponse
from django.db import connection

def health_check(request):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        db_status = "healthy"
    except Exception as e:
        db_status = f"unhealthy: {str(e)}"
    
    return JsonResponse({
        'status': 'healthy',
        'database': db_status,
        'timestamp': timezone.now().isoformat()
    })
```

## 🔄 CI/CD Pipeline

### GitHub Actions
```yaml
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Setup Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        python manage.py test
    
    - name: Deploy to Heroku
      uses: akhileshns/heroku-deploy@v3.12.12
      with:
        heroku_api_key: ${{secrets.HEROKU_API_KEY}}
        heroku_app_name: "your-app-name"
        heroku_email: "your-email@example.com"
```

## 📱 Scaling Considerations

### Horizontal Scaling
- Load balancer configuration
- Multiple application servers
- Database read replicas
- Redis clustering

### Vertical Scaling
- Increase server resources
- Optimize database queries
- Implement caching strategies
- Use CDN for static files

This deployment guide ensures your Django Library Project runs efficiently and securely in production environments.

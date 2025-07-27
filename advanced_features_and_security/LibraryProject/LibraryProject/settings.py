from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-@%&g81nq-hu6jq2jgym4h1%e!4!g$9cthm2-znxi2#gwn6b0#t'
DEBUG = False  # Set to False in production for security
ALLOWED_HOSTS = ['yourdomain.com', 'localhost', '127.0.0.1']  # Update with your production domain

# Security best practices and HTTPS enforcement
# SECURE_SSL_REDIRECT: Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS: Instruct browsers to only access the site via HTTPS for the specified time (1 year)
SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS: Apply HSTS to all subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD: Allow site to be included in browser preload lists
SECURE_HSTS_PRELOAD = True
# SECURE_BROWSER_XSS_FILTER: Enable browser’s XSS filtering
SECURE_BROWSER_XSS_FILTER = True
# X_FRAME_OPTIONS: Prevent site from being framed (clickjacking protection)
X_FRAME_OPTIONS = 'DENY'
# SECURE_CONTENT_TYPE_NOSNIFF: Prevent browsers from MIME-sniffing a response away from the declared content-type
SECURE_CONTENT_TYPE_NOSNIFF = True
# CSRF_COOKIE_SECURE: Ensure CSRF cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE: Ensure session cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'relationship_app',
    'bookshelf',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Custom user model
AUTH_USER_MODEL = 'bookshelf.CustomUser'


# Content Security Policy (CSP) example
# You can use django-csp or set headers manually in middleware/views
# Example for django-csp:
# INSTALLED_APPS += ['csp']
# MIDDLEWARE += ['csp.middleware.CSPMiddleware']
# CSP_DEFAULT_SRC = ("'self'",)
# CSP_SCRIPT_SRC = ("'self'",)
# CSP_STYLE_SRC = ("'self'",)

# Deployment Configuration:
# To enable HTTPS, configure your web server (e.g., Nginx, Apache) with SSL/TLS certificates.
# Example Nginx snippet:
#
# server {
#     listen 443 ssl;
#     server_name yourdomain.com;
#     ssl_certificate /etc/ssl/certs/yourdomain.com.crt;
#     ssl_certificate_key /etc/ssl/private/yourdomain.com.key;
#     ...
# }


# SECURE_PROXY_SSL_HEADER: Use this when behind a proxy/load balancer that sets X-Forwarded-Proto
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Security Review:
# - All cookies are secure and only sent over HTTPS.
# - All HTTP requests are redirected to HTTPS.
# - HSTS is enabled for 1 year, including subdomains and preload.
# - XSS, clickjacking, and MIME sniffing protections are enabled.
# - See SECURITY_README.md for further details and recommendations.

# Deployment Instructions for social_media_api

## 1. Production Settings
- Set `DEBUG = False` in `settings.py`.
- Set `ALLOWED_HOSTS` to your domain or server IP.
- Use environment variables for `SECRET_KEY` and database credentials.
- Add security settings:
  - `SECURE_BROWSER_XSS_FILTER = True`
  - `X_FRAME_OPTIONS = 'DENY'`
  - `SECURE_CONTENT_TYPE_NOSNIFF = True`
  - `SECURE_SSL_REDIRECT = True` (if using HTTPS)
- Set `STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')`
- Set `MEDIA_ROOT = os.path.join(BASE_DIR, 'media')`

## 2. Static Files
- Run `python manage.py collectstatic` before deployment.

## 3. Database
- Use PostgreSQL in production (Heroku provides this by default).
- Set `DATABASE_URL` in your environment variables.

## 4. Deployment (Heroku Example)
- Install Heroku CLI and login.
- Run `heroku create <your-app-name>`
- Set config vars: `heroku config:set SECRET_KEY=... DEBUG=False ALLOWED_HOSTS=...`
- Push code: `git push heroku main`
- Run migrations: `heroku run python manage.py migrate`
- Collect static files: `heroku run python manage.py collectstatic`

## 5. Gunicorn
- Make sure `gunicorn` is in your `requirements.txt`.
- Procfile is already set up: `web: gunicorn social_media_api.wsgi`

## 6. Monitoring
- Use Heroku dashboard or add-ons for logging and monitoring.

## 7. Final Testing
- Visit your live URL and test all endpoints.

---

For AWS, DigitalOcean, or other providers, follow their Django deployment guides and adjust settings accordingly.

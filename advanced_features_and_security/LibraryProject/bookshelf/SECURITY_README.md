# Security Best Practices for Django

## Secure Settings
- DEBUG is set to False in production.
- ALLOWED_HOSTS is configured for your domain.
- SECURE_BROWSER_XSS_FILTER, X_FRAME_OPTIONS, SECURE_CONTENT_TYPE_NOSNIFF are enabled for browser security.
- CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE are set to True to enforce HTTPS cookies.

## CSRF Protection
- All forms include `{% csrf_token %}` in templates (see `form_example.html`).

## Safe Data Access
- Views use Django ORM for all queries, preventing SQL injection.
- User input should be validated using Django forms (see `forms.py` for custom validation).

## Content Security Policy (CSP)
- Example CSP settings are provided in `settings.py` comments. Use `django-csp` for advanced CSP management.

## Testing
- Manually test forms and input fields for CSRF and XSS vulnerabilities.
- Review code for direct SQL usage and replace with ORM queries.

## Comments
- See comments in `settings.py`, `views.py`, and templates for details on each security measure.

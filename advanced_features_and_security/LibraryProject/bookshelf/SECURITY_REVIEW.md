# Security Review: HTTPS & Secure Redirects

## Security Measures Implemented
- All HTTP requests are redirected to HTTPS (`SECURE_SSL_REDIRECT = True`).
- HSTS is enabled for 1 year, including subdomains and preload (`SECURE_HSTS_SECONDS`, `SECURE_HSTS_INCLUDE_SUBDOMAINS`, `SECURE_HSTS_PRELOAD`).
- Session and CSRF cookies are only sent over HTTPS (`SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`).
- XSS, clickjacking, and MIME sniffing protections are enabled (`SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS`, `SECURE_CONTENT_TYPE_NOSNIFF`).
- Content Security Policy (CSP) guidance is provided in `settings.py`.

## How These Measures Secure the Application
- **HTTPS Redirects:** Prevents data interception by ensuring all traffic is encrypted.
- **HSTS:** Instructs browsers to only use HTTPS, protecting against protocol downgrade attacks.
- **Secure Cookies:** Prevents cookies from being sent over insecure connections.
- **Security Headers:** Protects against XSS, clickjacking, and MIME sniffing attacks.
- **CSP:** Reduces risk of XSS by restricting allowed sources for scripts and styles.

## Recommendations
- Regularly update SSL/TLS certificates and test server configuration.
- Monitor security advisories for Django and dependencies.
- Consider automated security testing and penetration testing for production deployments.

## Further Reading
- See `DEPLOYMENT_README.md` for web server configuration.
- See `settings.py` for all security-related settings and comments.

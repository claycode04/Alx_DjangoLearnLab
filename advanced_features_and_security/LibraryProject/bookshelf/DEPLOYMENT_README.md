# Deployment Configuration for HTTPS

## Web Server Setup
To enable HTTPS, configure your web server (e.g., Nginx, Apache) with SSL/TLS certificates.

### Example Nginx Configuration
```
server {
    listen 443 ssl;
    server_name yourdomain.com;
    ssl_certificate /etc/ssl/certs/yourdomain.com.crt;
    ssl_certificate_key /etc/ssl/private/yourdomain.com.key;
    # ...other settings...
}
```

### Example Apache Configuration
```
<VirtualHost *:443>
    ServerName yourdomain.com
    SSLEngine on
    SSLCertificateFile /etc/ssl/certs/yourdomain.com.crt
    SSLCertificateKeyFile /etc/ssl/private/yourdomain.com.key
    # ...other settings...
</VirtualHost>
```

## Additional Notes
- Ensure your certificates are valid and not expired.
- Test your server with SSL Labs or similar tools for best practices.
- Update your Django `ALLOWED_HOSTS` to match your domain.

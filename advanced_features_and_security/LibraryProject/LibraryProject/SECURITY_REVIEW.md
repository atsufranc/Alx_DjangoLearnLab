# Security Review: HTTPS & Secure Headers

## HTTPS Enforcement
- `SECURE_SSL_REDIRECT = True`: All HTTP requests are redirected to HTTPS.
- `SECURE_HSTS_SECONDS = 31536000`: Instructs browsers to only use HTTPS for one year.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Applies HSTS to all subdomains.
- `SECURE_HSTS_PRELOAD = True`: Allows site to be included in browser preload lists.

## Secure Cookies
- `SESSION_COOKIE_SECURE = True`: Session cookies only sent over HTTPS.
- `CSRF_COOKIE_SECURE = True`: CSRF cookies only sent over HTTPS.

## Secure Headers
- `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME-type sniffing.
- `SECURE_BROWSER_XSS_FILTER = True`: Enables browser XSS filter.

## Deployment
- Example Nginx config provided in `DEPLOYMENT_HTTPS.md` for SSL setup.
- Ensure SSL/TLS certificates are valid and renewed regularly.

## Review & Recommendations
- All major Django HTTPS and header security settings are enabled.
- For production, set `ALLOWED_HOSTS` to your real domain(s).
- Regularly review Django and server security documentation for updates.
- Consider using additional security middleware (e.g., django-csp for Content Security Policy).

---
For more, see: https://docs.djangoproject.com/en/5.0/topics/security/

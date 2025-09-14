# Security Measures in This Django Project

## settings.py
- `DEBUG = False` in production to prevent sensitive data leaks.
- `ALLOWED_HOSTS` restricts which hosts can serve the app.
- `SECURE_BROWSER_XSS_FILTER = True` enables browser XSS protection.
- `X_FRAME_OPTIONS = 'DENY'` prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True` prevents MIME-type sniffing.
- `CSRF_COOKIE_SECURE = True` and `SESSION_COOKIE_SECURE = True` ensure cookies are only sent over HTTPS.
- (Optional) Content Security Policy (CSP) can be enabled with django-csp for XSS protection.

## Templates
- All forms must include `{% csrf_token %}` to protect against CSRF attacks.
- Example:
  ```html
  <form method="post">
      {% csrf_token %}
      <!-- form fields -->
  </form>
  ```

## Views
- All user input is handled via Django ORM and not via raw SQL, preventing SQL injection.
- Use Django forms or validate/sanitize user input before saving to the database.

## Testing
- Manually test forms for CSRF protection (submitting without token should fail).
- Test for XSS by entering script tags in form fields (should be escaped in output).
- Test for SQL injection by entering SQL in form fields (should not affect queries).

## Comments
- All security settings and practices are commented in the code for clarity.

---
For more, see Django's official security checklist: https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

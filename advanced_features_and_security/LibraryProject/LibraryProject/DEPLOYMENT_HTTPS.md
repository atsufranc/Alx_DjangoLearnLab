# Deployment Configuration for HTTPS (Example: Nginx)

1. Obtain an SSL/TLS certificate (e.g., from Let's Encrypt).
2. Configure your web server to use SSL. Example Nginx config:

```
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name yourdomain.com www.yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /path/to/your/project;
    }
    location / {
        include proxy_params;
        proxy_pass http://unix:/path/to/your/project.sock;
    }
}
```

3. Restart Nginx after making changes:
```
sudo systemctl restart nginx
```

4. Ensure Django's `settings.py` is configured for HTTPS (see main project settings).

---
For Apache or other servers, see Django's deployment docs: https://docs.djangoproject.com/en/5.0/howto/deployment/

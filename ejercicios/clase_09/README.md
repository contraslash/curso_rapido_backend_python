# Run gunicorn local

```bash
cd blog_flask
gunicorn --bind 127.0.0.1:9000 wsgi:application --daemon
```

Apache modules

```bash
sudo a2enmod proxy
sudo a2enmod proxy_http
```

```xml
<VirtualHost *:80>
    ProxyPreserveHost On

    ProxyPass / http://127.0.0.1:8000/
    ProxyPassReverse / http://127.0.0.1:8000/
</VirtualHost>
```

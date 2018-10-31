Title: Despliegue
Author: Mauricio Collazos
Date: 2018-10-19
![]()
---
class: center, middle, light, first-slide
# Despliegue
## Mauricio Collazos
.footnote[]
---
# Modelos de servicio

- IaaS
- PaaS
- SaaS (???)
- FaaS
  
---
# IaaS

Bare Metal

Configuración bajo un sistema Unix
Pet vs Cattle
- [Chef](https://www.chef.io/chef/)
- [Puppet](https://puppet.com/)
- [Ansible](https://www.ansible.com/)
---
# PaaS
- [Heroku](https://www.heroku.com/)
- [Google App Engine](https://cloud.google.com/appengine/docs/)
- [Python Anywhere](https://www.pythonanywhere.com/)
---
# FaaS
- [Zappa](https://github.com/Miserlou/Zappa)
- [Chalice](https://github.com/aws/chalice)
---
# Contenedores
- [Docker](https://www.docker.com/)
- [Compose](https://docs.docker.com/compose/)
- [Swarm](https://docs.docker.com/engine/swarm/)
- [Kubernetes](https://kubernetes.io/)

---
# [GUnicorn](https://gunicorn.org/)
Flask 
`wsgi.py`
```bash
from blog_project import create_app

app = create_app()
```

`gunicorn wsgi:app`

Django

```bash
gunicorn project_name.wsgi
```

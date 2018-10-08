Author: Mauricio Collazos
Title: Django Cheat Sheet
Date: 2018-10-08
---
![]()
---
class: center, middle
# Django Cheat Sheet
## Mauricio Collazos
---

**Instalar Django**

Conda
```bash
conda install -c anaconda
```

Virtualenv
```bash
pip install django
```
**Crear un Proyecto**

Este comando comando crea una carpeta con los archivos básicos del proyecto 
```bash
django-admin startproject [nombre_del_proyecto]
```
---

**Crear una Applicación**

Este comando crea una carpeta con los archivos básicos de la aplicación
```bash
django-admin startapp [nombre_de_la_aplicación]
```

**Ejecutar el servidor**

```bash
cd carpeta_del_proyecto
python manage.py runserver
```

---
**Replicar ambiente**

Conda
```bash
conda install --file environment.yml
```

Virtualenv
```bash
pip install -r requirements.txt
```
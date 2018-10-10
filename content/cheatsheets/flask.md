Author: Mauricio Collazos
Title: Flask Cheat Sheet
Date: 2018-10-10
---
![]()
---
class: center, middle
# Flask Cheat Sheet
## Mauricio Collazos
---

**Instalar Django**

Conda
```bash
conda install -c flask
```

Virtualenv
```bash
pip install flask
```
**Crear un Proyecto**
 
```bash
mkdir [carpeta_del_proyecto]
cd [carpeta_del_proyecto]
mkdir [modulo_del_proyecto]
cd [modulo_del_proyecto]
# x-nix 
touch __init__.py
touch app.py
# windows
type null > __init__.py
type null > app.py
```
---

**Crear una Applicación**

```bash
cd [carpeta_del_proyecto]
cd [modulo_del_proyecto]
mkdir [nombre_de_la_aplicación]
cd nombre_de_la_applicación
# x-nix 
touch __init__.py
touch models.py
touch views.py

# windows
type null > __init__.py
type null > models.py
type null > views.py

```

**Ejecutar el servidor**

```bash
cd carpeta_del_proyecto
# x-nix 
FLASK_RUN_PORT=8000 FLASK_DEBUG=1 FLASK_APP=[modulo_del_proyecto] flask run
# windows
set FLASK_RUN_PORT=8000 
set FLASK_DEBUG=1 
set FLASK_APP=[modulo_del_proyecto]
flask run
```
---
**Estructura de un proyecto en flask**
```bash
├── README.md
└── blog
    ├── __init__.py
    ├── app.py
    ├── applications
    │   ├── __init__.py
    │   └── blog
    │       ├── __init__.py
    │       ├── conf.py
    │       ├── models.py
    │       ├── templates
    │       │   ├── create.html
    │       │   ├── detail.html
    │       │   ├── list.html
    │       │   └── update.html
    │       ├── urls.py
    │       └── views.py
    ├── config.py
    ├── database.py
    ├── db.sqlite3
    ├── static
    │   └── style.css
    └── templates
        └── base.html
```

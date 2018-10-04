# Blog flask


La aplicación debe ejecutarse desde la carpeta padre del proyecto
Para ejecutar la aplicación
```bash
FLASK_RUN_PORT=8000 FLASK_DEBUG=1 FLASK_APP=blog_flask flask run
```

Para usuarios windows
```bash
set FLASK_RUN_PORT=8000 
set FLASK_DEBUG=1 
set FLASK_APP=blog_flask
flask run
```

Para crear posts

```python
from blog_flask import (
    app as blog_app,
    models as blog_models,
    database as blog_database
)
app = blog_app.create_app()
app.app_context().push()
p1 = blog_models.Post()
p1.id = 1
p1.title = "Hello world"
p1.body = "lorem ipsum"
db = blog_database.db
db.session.add(p1)
db.session.commit()
```

Para tener todos los post
```python
from blog_flask import (
    app as blog_app,
    models as blog_models,
    database as blog_database
)
app = blog_app.create_app()
db = blog_database.db
blog_models.Post.query.all()
```
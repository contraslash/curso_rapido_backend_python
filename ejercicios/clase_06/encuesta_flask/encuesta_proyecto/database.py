# Simplemente se inicializa la base de datos
from flask_sqlalchemy import SQLAlchemy

# Este objeto db será llamado por todos los modelos de los blueprints
db = SQLAlchemy()
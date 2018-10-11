from datetime import datetime

from encuesta_proyecto.database import db

# Definición de los modelos
class Survey(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(80),
        nullable=False
    )
    last_name = db.Column(
        db.String(80),
        nullable=False
    )

    def __str__(self):
        return "{}".format(self.title)
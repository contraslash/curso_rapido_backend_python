import wtforms

class Encuesta(wtforms.Form):
    name = wtforms.StringField('Name', [wtforms.validators.Length(min=6, max=80)])
    last_name = wtforms.StringField('Last Name', [wtforms.validators.Length(min=6, max=80)])

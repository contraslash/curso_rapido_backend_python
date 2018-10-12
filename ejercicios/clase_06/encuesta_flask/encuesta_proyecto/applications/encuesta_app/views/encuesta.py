from flask.views import View
from flask.templating import render_template
from flask.helpers import url_for, request, flash
from flask.globals import g
from werkzeug.utils import redirect

from .. import (
    conf,
    models,
    forms
)


class List(View):

    def dispatch_request(self):
        context = dict()
        context["encuestas"] = models.Survey.query.all()
        context["crear_encuesta"] = conf.get_prefixed_url(conf.SURVEY_CREATE_URL_NAME)
        context["detalle_encuesta"] = conf.get_prefixed_url(conf.SURVEY_DETAIL_URL_NAME)
        return render_template('encuesta/lista.html', **context)


class Crear(View):
    #  Defina que métodos va a recibir
    methods = ["GET", "POST"]
    # Todas las vistas deben implementar el método dispatch_request
    def dispatch_request(self):
        context = dict()
        form = forms.Encuesta(request.form)
        if request.method == 'POST' and form.validate():
            survey = models.Survey(
                name=form.name.data,
                last_name=form.last_name.data,
            )
            models.db.session.add(survey)
            models.db.session.commit()
            flash('Thanks for registering')
            return redirect(url_for(conf.get_prefixed_url(conf.SURVEY_LIST_URL_NAME)))
        # Que debe retornar una vista renderizada
        context['form'] = form
        return render_template('encuesta/crear.html', **context)


class Detalle(View):
    def dispatch_request(self, encuesta_id):
        context = dict()
        context["encuesta"] = models.Survey.query.filter_by(id=encuesta_id).first_or_404()
        context["actualizar_encuesta"] = conf.get_prefixed_url(conf.SURVEY_UPDATE_URL_NAME)
        context["eliminar_encuesta"] = conf.get_prefixed_url(conf.SURVEY_DELETE_URL_NAME)
        print(context)

        return render_template('encuesta/detalle.html', **context)


class Actualizar(View):
    methods = ["GET", "POST"]
    def dispatch_request(self, encuesta_id):
        context = dict()
        context["survey"] = models.Survey.query.filter_by(id=encuesta_id).first_or_404()
        print(context)
        if request.method == 'POST':
            form = forms.Encuesta(request.form)
            if  form.validate():
                survey = context['survey']
                survey.name=form.name.data
                survey.last_name=form.last_name.data
                models.db.session.add(survey)
                models.db.session.commit()
                flash('Thanks for registering')
                return redirect(url_for(conf.get_prefixed_url(conf.SURVEY_LIST_URL_NAME)))
        # Que debe retornar una vista renderizada
        else:
            form = forms.Encuesta(
                name=context['survey'].name,
                last_name=context['survey'].last_name
            )
        context['form'] = form
        return render_template('encuesta/actualizar.html', **context)


class Eliminar(View):
    def dispatch_request(self, encuesta_id):
        models.Survey.query.filter_by(id=encuesta_id).delete()
        models.db.session.commit()
        return redirect(
            url_for(
                conf.get_prefixed_url(conf.SURVEY_LIST_URL_NAME)
            )
        )
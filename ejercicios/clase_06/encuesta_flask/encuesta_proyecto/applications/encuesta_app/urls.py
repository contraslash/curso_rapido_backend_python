from . import (
    bp,
    conf
)

from .views import (
    encuesta as encuesta_views
)


# Creamos esta función para poder cargarle al blueprint todas las urls, este método se llama en el __init__.py
# del blueprint
def load_urls():
    bp.add_url_rule(
        "/",
        view_func=encuesta_views.List.as_view(conf.SURVEY_LIST_URL_NAME)
    )
    bp.add_url_rule(
        "/crear/",
        view_func=encuesta_views.Crear.as_view(conf.SURVEY_CREATE_URL_NAME)
    )
    bp.add_url_rule(
        "/<int:encuesta_id>/",
        view_func=encuesta_views.Detalle.as_view(conf.SURVEY_DETAIL_URL_NAME)
    )
    bp.add_url_rule(
        "/<int:encuesta_id>/actualizar",
        view_func=encuesta_views.Actualizar.as_view(conf.SURVEY_UPDATE_URL_NAME)
    )
    bp.add_url_rule(
        "/<int:encuesta_id>/eliminar",
        view_func=encuesta_views.Eliminar.as_view(conf.SURVEY_DELETE_URL_NAME)
    )
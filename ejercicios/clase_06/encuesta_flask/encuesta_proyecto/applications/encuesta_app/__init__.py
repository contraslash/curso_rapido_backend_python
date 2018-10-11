import functools
import os

from flask.blueprints import Blueprint

from . import conf


bp = Blueprint(
    conf.SURVEY_PREFIX_URL,
    __name__,
    url_prefix='/encuestas', # Prefijo de las urls
    template_folder=os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        "templates"
    )
)

# flask does not load our inner schema so we need to tell flask
# to consider the schemas loading the urls and models

# Manera de cargar las urls y los models
from .urls import load_urls
load_urls()
from . import models
import functools
import os

from flask.blueprints import Blueprint

from flask_restful import Api


bp = Blueprint(
    'blog_project',
    __name__,
    url_prefix='/',
    template_folder=os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        "templates"
    )
)

# flask does not load our inner schema so we need to tell flask
# to consider the schemas loading the urls and models

from .urls import load_urls
load_urls()
from . import models

api_bp = Api(bp, "api")
from .urls_api import load_urls as load_urls_api
load_urls_api()
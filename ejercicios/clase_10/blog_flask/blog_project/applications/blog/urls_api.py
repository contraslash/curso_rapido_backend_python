from . import (
    api,
    api_bp
)


def load_urls():
    api_bp.add_resource(api.Post, '/post/')
    api_bp.add_resource(api.PostWithId, '/post/<int:id>')
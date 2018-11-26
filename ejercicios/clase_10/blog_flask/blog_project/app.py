from flask import Flask
from flask_login import LoginManager
from .database import db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    from .applications.blog import bp as blog_bp
    app.register_blueprint(blog_bp)
    from .applications.auth import (
        bp as auth_bp,
        models as auth_models
    )

    app.register_blueprint(auth_bp)
    print("Initializing DB")
    db.init_app(app)
    with app.test_request_context():
        db.create_all()
    print("DB Initialized successfully")

    print("Initializing Login Manager")
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return auth_models.User.query.filter_by(id=user_id).first()
    print("Login Manager Initialized successfully")
    return app
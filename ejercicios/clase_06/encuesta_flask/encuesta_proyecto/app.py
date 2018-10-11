from flask import Flask

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
    # Aquí cargue los blueprints
    from .applications.encuesta_app import bp as encuestas_blueprint
    app.register_blueprint(encuestas_blueprint)
    print("Initializing DB")
    db.init_app(app)
    with app.test_request_context():
        db.create_all()
    print("DB Initialized successfully")

    return app
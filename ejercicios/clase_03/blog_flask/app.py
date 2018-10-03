from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .database import db

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    print("Initializing DB")
    db.init_app(app)
    from .models import Post
    with app.test_request_context():
        db.create_all()
    print("DB Initialized successfully")

    @app.route("/")
    def index():
        all_posts = Post.query.all()
        post_titles = ",".join([post.title for post in all_posts])
        return post_titles
    return app

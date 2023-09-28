import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS
from video_api.config import App_Config

db = SQLAlchemy()

def create_app():
    """
    Create a new instance of the app with the given configuration.

    :param config_class: configuration class
    :return: app
    """
    # Initialize Flask-
    app = Flask(__name__)
    app.config.from_object(App_Config)

    # Initialize CORS
    CORS(app, supports_credentials=True)
    # Initialize SQLAlchemy
    db.init_app(app)

    from video_api.video.views import videos
    
    app.register_blueprint(videos)

    # create db tables from models if not exists
    with app.app_context():
        db.create_all()

    return app
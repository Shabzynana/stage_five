import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


app.config['SECRET_KEY'] = ''

########################   ####################

        # SQL DATABASE AND MODELS

##########################################
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_pre_ping": True}
app.config['SQLALCHEMY_DATABASE_URI'] = ""
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db,render_as_batch=True)






from music_app.video.views import videos

app.register_blueprint(videos)

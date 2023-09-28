from flask import url_for,flash,redirect,request,Blueprint,jsonify
from video_api.models import User


videos = Blueprint('videos',__name__,)

@videos.route('/', methods=['GET','POST'])
def save_video():
    pass

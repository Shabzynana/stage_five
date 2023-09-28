from video_api import db
from uuid import uuid4


def get_uuid():
    """Generate a unique id using uuid4()"""
    return uuid4().hex


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.String(60), primary_key=True, default=get_uuid)
    email = db.Column(db.String(64),unique=False,index=True)
    video_url = db.Column(db.String(64),nullable=False)


    def __init__(self,email,video_url):

        self.email = email
        self.video_url = video_url

    def __repr__(self):
        return f" email: {self.email}"

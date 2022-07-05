from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


# initialize app
from sqlalchemy import func

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


# Product class
class Post(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    user_email = db.Column(db.String(100), unique=True, nullable=False)
    post_description = db.Column(db.String(200))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    number_of_likes = db.Column(db.INTEGER)
    post_comments = db.Column(db.String(500))

    def __init__(self, user_email, post_description, created_at, number_of_likes, post_comments):
        self.user_email = user_email
        self.post_description = post_description
        self.created_at = created_at
        self.number_of_likes = number_of_likes
        self.post_comments = post_comments


# post schema
class PostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_email', 'post_description', 'created_at', 'number_of_likes', 'post_comments')


# initialize schema

post_schema = PostSchema()
multi_post_schema = PostSchema(many=True)


# command to run shell command

'''
  from domain.model import *
  db.create_all()
'''


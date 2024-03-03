from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import TIMESTAMP 
import datetime 

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    """User Model"""
    __tablename__ = 'user_tb'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    image_url = db.Column(db.String(30), default='https://cdn-icons-png.flaticon.com/512/9131/9131529.png')

    def __repr__(self):
        e = self
        return f"<User {e.id} {e.first_name} {e.last_name} {e.image_url}>"

class Post(db.Model):
    """Post Model"""
    __tablename__ = "post_tb"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(TIMESTAMP, nullable=False, default=datetime.datetime.utcnow)

    user_id = db.Column(db.Text, db.ForeignKey('user_tb.id'))
    user = db.relationship('User', backref='posts')

    # direct navigation: post -> tag & visa versa
    tags = db.relationship('Tag', secondary='posts_tags_tb', backref='posts')

    def __repr__(self):
        e = self
        return f"<Post {e.id} {e.title} {e.content} {e.created_at}>"
    
class Tag(db.Model):
    """Tag Model"""
    __tablename__ = "tag_tb"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)

    def __repr__(self):
        e = self
        return f"<Tag {e.id} {e.name}>"
    
class PostTag(db.Model):
    """Mapping tags to posts"""
    __tablename__ = "posts_tags_tb"

    post_id = db.Column(db.Integer, db.ForeignKey("post_tb.id"), primary_key=True)
    tag_id = db.Column(db.Text, db.ForeignKey("tag_tb.id"), primary_key=True)

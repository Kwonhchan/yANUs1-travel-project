from web import db
from flask_login import UserMixin
from datetime import datetime
class User(db.Model,UserMixin):
    id = db.Column(db.String(120),primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nickname = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200))
    phone = db.Column(db.String(11), unique=True, nullable=False)
    notes = db.relationship('Note')


class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(2000))
    datetime = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
    user_id = db.Column(db.String(120), db.ForeignKey('user.id'))
from app import db
from datetime import datetime


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    subejct = db.Column(db.String, nullable=True)
    message = db.Column(db.String, nullable=True)
    respon = db.Column(db.Integer, default=True)
    date_send = db.Column(db.DateTime, default=datetime.utcnow()) # or datetime.now()


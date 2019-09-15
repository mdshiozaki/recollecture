from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Collect(db.Model):
    __tablename__ = 'recollecture'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(250))
    transcript = db.Column(db.String(250))
    keywords = db.Column(db.String(250))

    def __init__(self, name, transcript, keywords):
        self.name = name
        self.transcript = transcript
        self.keywords = keywords

class CollectSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    transcript = fields.String()
    keywords = fields.String()
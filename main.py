from enum import unique
from flask import Flask, request, jsonify
from sqlalchemy import ForeignKey
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)
db = SQLAlchemy(app)


class Articulo(db.Model):
    article_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    # ¿No sería chevere saber cuántos hay?
    # ¿No sería chevere saber cuánto cuesta?


class Venta(db.Model):
    article_id = db.Column(db.Integer, unique=True, nullable=False)
    fecha = db.Column(db.DateTime)
    cantidad = db.Column(db.Float)

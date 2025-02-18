from enum import unique
from flask import Flask, request, jsonify
from sqlalchemy import ForeignKey
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)
db = SQLAlchemy(app)


class Articulo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String)
    cantidad = db.Column(db.Integer)
    precio = db.Column(db.Float)


class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha = db.Column(db.DateTime)


class ArticulosVenta(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    venta = db.Column(db.Integer, ForeignKey('venta.id'))
    articulo = db.Column(db.Integer, ForeignKey('articulo.id'))
    cantidad = db.Column(db.Integer)

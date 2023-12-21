from app.app import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(60), nullable=False)
    color = db.Column(db.String(6), nullable=False)
    budget_type = db.Column(db.Boolean, nullable=False, default=True) # True - Income

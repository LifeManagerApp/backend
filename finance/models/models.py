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
    default = db.Column(db.Boolean, nullable=False, default=False)


class UsersCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)


class MoneyManagement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    users_category_id = db.Column(db.Integer, db.ForeignKey('users_category.id', ondelete='CASCADE'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    comment = db.Column(db.String, nullable=True)
    budget_type = db.Column(db.Boolean, nullable=False, default=True)  # True - Income
    date = db.Column(db.Date)

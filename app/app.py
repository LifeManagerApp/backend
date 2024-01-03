from base.base_db import DBConnection
from base.base_jwt import JWT

from flask import Flask
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DBConnection.CONNECTION
app.config['JWT_SECRET_KEY'] = JWT.JWT_SECRET_KEY

jwt = JWTManager(app)

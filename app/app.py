import os
from dotenv import load_dotenv

if os.path.exists('../../.env'):
    load_dotenv('../../.env')
    print('.env loaded successful')
else:
    print(os.getcwd())
    load_dotenv('.env')
    print('fuck you')


DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_MAIN_DATABASE = os.getenv("DB_MAIN_DATABASE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


from flask import Flask
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_MAIN_DATABASE}"
app.config['JWT_SECRET_KEY'] = 'your_secret_key'

jwt = JWTManager(app)

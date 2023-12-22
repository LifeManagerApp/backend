from flask import request
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token

from finance.routs.common import routes
from finance.routs.auth.auth import Auth


@routes.route('/auth', methods=['POST'])
def auth():
    access_token = None

    data = request.get_json()

    login = data.get('login')
    password = data.get('password')

    success = Auth.auth(login=login, password=password)
    if success:
        access_token = create_access_token(identity=login)

    return {'success': success, 'access_token': access_token}


@routes.route('/registration', methods=['POST'])
def registration():
    access_token = None

    data = request.get_json()

    login = data.get('login')
    password = data.get('password')
    email = data.get('email')

    success = Auth.registration(login=login, password=password, email=email)
    if success:
        access_token = create_access_token(identity=login)

    return {'success': success, 'access_token': access_token}

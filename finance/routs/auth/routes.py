from flask import request
from flask_jwt_extended import create_access_token
from finance.routs.common_rotes import routes
from finance.routs.auth.auth import Auth


@routes.route('/auth', methods=['POST'])
async def auth():
    access_token = None

    data = request.get_json()

    login = data.get('login')
    password = data.get('password')

    success = await Auth.auth(login=login, password=password)
    if success:
        access_token = create_access_token(identity=login)

    return {'success': success, 'access_token': access_token}


@routes.route('/registration', methods=['POST'])
async def registration():
    access_token = None

    data = request.get_json()

    login = data.get('login')
    password = data.get('password')
    email = data.get('email')

    success = await Auth.registration(login=login, password=password, email=email)
    if success:
        access_token = create_access_token(identity=login)

    return {'success': success, 'access_token': access_token}

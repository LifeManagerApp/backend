from flask import request
from finance.routs.common import routes
from finance.routs.auth.auth import Auth


@routes.route('/auth', methods=['POST'])
def auth():
    data = request.get_json()

    login = data.get('login')
    password = data.get('password')
    return {'success': Auth.auth(login=login, password=password)}


@routes.route('/registration', methods=['POST'])
def registration():
    data = request.get_json()

    login = data.get('login')
    password = data.get('password')
    email = data.get('email')

    return {'success': Auth.registration(login=login, password=password, email=email)}

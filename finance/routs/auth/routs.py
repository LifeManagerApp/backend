from flask import request
from finance.routs.common import routes

from finance.models.models import User, Categories, db


@routes.route('/auth', methods=['POST'])
def auth():
    data = request.get_json()

    login = data.get('login')
    password = data.get('password')

    user = User.query.filter_by(login=login, password=password).first()

    if user:
        return {'success': True}
    return {'success': False}


@routes.route('/registration', methods=['POST'])
def registration():
    data = request.get_json()

    login = data.get('login')
    password = data.get('password')
    email = data.get('email')

    try:
        user = User(email=email, password=password, login=login)
        db.session.add(user)
        db.session.commit()
    except:
        db.session.rollback()
        return {'success': False}

    return {'success': True}



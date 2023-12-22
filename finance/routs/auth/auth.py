from finance.models.models import User, db


class Auth:
    @staticmethod
    def auth(login: str, password: str) -> bool:
        user = User.query.filter_by(login=login, password=password).first()
        if user:
            return True
        return False

    @staticmethod
    def registration(email: str, login: str, password: str) -> bool:
        try:
            user = User(email=email, password=password, login=login)
            db.session.add(user)
            db.session.commit()
        except:
            db.session.rollback()
            return False
        return True


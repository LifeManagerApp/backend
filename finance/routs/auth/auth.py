from finance.models.models import User, db, Categories, UsersCategory
from base.base_hash import Hash


class Auth(Hash):

    @classmethod
    def auth(cls, login: str, password: str) -> bool:
        user = User.query.filter_by(login=login, password=cls.hash_password(password)).first()
        if user:
            return True
        return False

    @staticmethod
    def get_user(login: str) -> User:
        user = User.query.filter_by(login=login).first()
        return user

    @classmethod
    def registration(cls, email: str, login: str, password: str) -> bool:
        try:
            user = User(email=email, password=cls.hash_password(password), login=login)
            db.session.add(user)
            db.session.commit()
        except:
            db.session.rollback()
            return False

        default_categories = Categories.query.filter_by(default=True).all()
        user_category = []
        for category in default_categories:
            user_category.append(UsersCategory(user_id=user.id, category_id=category.id))

        db.session.add_all(user_category)
        db.session.commit()
        return True


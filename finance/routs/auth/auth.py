from finance.models.models import User, db, Categories, UsersCategory
from base.base_hash import Hash
from common.logger import logger


class Auth(Hash):

    @classmethod
    async def auth(cls, login: str, password: str) -> bool:
        user = User.query.filter_by(
            login=login,
            password=await cls.hash_password(password)
        ).first()
        if user:
            return True
        return False

    @staticmethod
    async def get_user(login: str) -> User:
        user = User.query.filter_by(login=login).first()
        return user

    @classmethod
    async def registration(cls, email: str, login: str, password: str) -> bool:
        try:
            user = User(
                email=email,
                password=await cls.hash_password(password),
                login=login
            )
            db.session.add(user)
            db.session.commit()
        except Exception as ex:
            logger.error(ex)
            db.session.rollback()
            return False

        default_categories = Categories.query.filter_by(default=True).all()
        user_category = []
        for category in default_categories:
            user_category.append(
                UsersCategory(
                    user_id=user.id,
                    category_id=category.id
                )
            )

        db.session.add_all(user_category)
        db.session.commit()
        return True

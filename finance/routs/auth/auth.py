from finance.models.models import User, db, Categories, UsersCategory
from base.base_hash import Hash
from common.logger import logger
from common.crypto import Crypto


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

    @classmethod
    async def tg_auth(cls, login: str, tg_id: str) -> bool:
        user = await cls.get_user(login=login)

        if user is None:
            await cls.tg_registration(login=login, tg_id=tg_id)
        return True

    @staticmethod
    async def get_user(login: str) -> User:
        user = User.query.filter_by(login=login).first()
        return user

    # TODO: чекнуть тип возвращаемых данных
    @staticmethod
    async def get_default_categories():
        default_categories = Categories.query.filter_by(default=True).all()
        return default_categories

    @classmethod
    async def set_default_user_categories(cls, user: User) -> bool:
        default_categories = await cls.get_default_categories()

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

        success = await cls.set_default_user_categories(user=user)

        return success

    @classmethod
    async def tg_registration(cls, login: str, tg_id: str):
        #tg_id = Crypto.decode(tg_id)
        try:
            user = User(
                tg_id=tg_id,
                login=login
            )
            db.session.add(user)
            db.session.commit()
        except Exception as ex:
            logger.error(ex)
            db.session.rollback()
            return False

        success = await cls.set_default_user_categories(user=user)

        return success

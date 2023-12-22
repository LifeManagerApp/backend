from finance.models.models import User, Categories
from finance.models.db_worker import DBWorker


class UserProperties(DBWorker):

    def user_add(self, login, password, email):
        user = User(login=login, password=password, email=email)
        return self.write(model_object=user)


    #TODO Создание юзера

    #TODO Получение свойств юзера по логину

    #TODO Получение категорий пользователя
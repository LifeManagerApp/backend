from finance.models.models import db, Categories, UsersCategory, User, MoneyManagement
from finance.routs.auth.auth import Auth


class MoneyManagementHandling:

    @staticmethod
    async def get_money_management(login, date_from, date_to):
        results = db.session.query(MoneyManagement). \
            join(UsersCategory). \
            join(User). \
            join(Categories). \
            filter(User.login == login). \
            filter(MoneyManagement.date.between(date_from, date_to)).all()

        print(results)
        return results

    # TODO: Transfer data using NAMED TUPLES

    @staticmethod
    async def set_money_management(users_category_id, user_amount, comment, budget_type, date):

        money_management_notion = MoneyManagement(users_category_id=users_category_id,
                                                  user_amount=user_amount, comment=comment,
                                                  budget_type=budget_type, date=date)

        try:
            db.session.add(money_management_notion)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False


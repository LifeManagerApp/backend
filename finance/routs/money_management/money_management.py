from finance.models.models import db, Categories, UsersCategory, User, MoneyManagement
from finance.routs.auth.auth import Auth
from finance.routs.money_management.models.money_manage_history import MoneyManageHistoryParams

from finance.routs.money_management.models.set_money_manager_struct import SetMoneyManageParams


class MoneyManagementHandling:
    @staticmethod
    async def get_money_management_history(history_params: MoneyManageHistoryParams):
        # TODO: дописать методы на получение истории по категории, по приходам/уходам
        money_management_data = MoneyManagement.query \
            .join(User, MoneyManagement.user_id == User.id) \
            .join(UsersCategory, MoneyManagement.users_category_id == UsersCategory.id) \
            .join(Categories, UsersCategory.category_id == Categories.id) \
            .filter(User.login == history_params.login) \
            .filter(MoneyManagement.date >= history_params.date_from) \
            .filter(MoneyManagement.date <= history_params.date_to) \
            .add_columns(Categories.category_name) \
            .order_by(MoneyManagement.date) \
            .all()

        response = []

        total_sum = 0

        for data in money_management_data:
            data_dict_temp = {
                "id": data[0].id,
                "user_id": data[0].user_id,
                "users_category_id": data[0].users_category_id,
                "amount": data[0].amount,
                "comment": data[0].comment,
                "budget_type": data[0].budget_type,
                "date": data[0].date,
                "category_name": data[1]
            }
            total_sum += data[0].amount
            response.append(data_dict_temp)

        return response, total_sum

    @staticmethod
    async def set_money_management(
            set_money_manage_params: SetMoneyManageParams
    ):
        user = await Auth.get_user(set_money_manage_params.login)

        money_management_notion = MoneyManagement(
            user_id=user.id,
            users_category_id=set_money_manage_params.users_category_id,
            amount=set_money_manage_params.amount,
            comment=set_money_manage_params.comment,
            budget_type=set_money_manage_params.budget_type,
            date=set_money_manage_params.date
        )

        try:
            db.session.add(money_management_notion)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False

    @staticmethod
    async def total_balance(login: str):
        balance = db.session.query(
            db.func.sum(
                db.case(
                    (MoneyManagement.budget_type == True, MoneyManagement.amount),
                    else_=-MoneyManagement.amount
                )
            )
        ).join(User).filter(User.login == login).scalar()

        return balance

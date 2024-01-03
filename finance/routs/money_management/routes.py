from flask import request
from finance.routs.common import routes
from flask_jwt_extended import jwt_required, get_jwt_identity
from finance.routs.money_management.money_management import MoneyManagementHandling


@routes.route('/money_management', methods=['POST', 'GET'])
@jwt_required()
def money_management():
    login = get_jwt_identity()

    if request.method == 'POST':
        data = request.get_json()

        users_category_id = data.get('users_category_id')
        user_amount = data.get('user_amount')
        comment = data.get('comment')
        budget_type = data.get('budget_type')
        date = data.get('date')

        accept = MoneyManagementHandling.set_money_management(users_category_id=users_category_id,
                                                     user_amount=user_amount, comment=comment,
                                                     budget_type=budget_type, date=date)

        return {'Success': accept}

    if request.method == 'GET':
        date_from = request.args.get('date_from')
        date_to = request.args.get('date_to')
        MoneyManagementHandling.get_money_management(login=login, date_from=date_from, date_to=date_to)

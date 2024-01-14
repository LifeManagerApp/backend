from flask import request
from finance.routs.common_rotes import routes
from flask_jwt_extended import jwt_required, get_jwt_identity

from finance.routs.money_management.models.money_manage_history import MoneyManageHistoryParams
from finance.routs.money_management.models.set_money_manager_struct import SetMoneyManageParams
from finance.routs.money_management.money_management import MoneyManagementHandling


@routes.route('/money_management', methods=['POST'])
@jwt_required()
async def money_management():
    login = get_jwt_identity()

    data = request.get_json()
    set_money_manage_params = SetMoneyManageParams(
        login=login,
        users_category_id=data.get('users_category_id'),
        amount=data.get('amount'),
        comment=data.get('comment'),
        budget_type=data.get('budget_type'),
        date=data.get('date'),
    )

    accept = await MoneyManagementHandling.set_money_management(
        set_money_manage_params=set_money_manage_params
    )

    return {'Success': accept}


@routes.route('/money_management/history', methods=['GET'])
@jwt_required()
async def history():
    login = get_jwt_identity()

    history_params = MoneyManageHistoryParams(
        login=login,
        date_from=request.args.get('date_from'),
        date_to=request.args.get('date_to'),
        category=request.args.get('category'),
        income=request.args.get('income')
    )
    management_data = await MoneyManagementHandling.get_money_management_history(
        history_params=history_params
    )

    return {'Success': True, "data": {"history": management_data, "total_sum": management_data[1]}}


@routes.route('/money_management/total_balance', methods=['GET'])
@jwt_required()
async def total_balance():
    login = get_jwt_identity()

    balance = await MoneyManagementHandling.total_balance(
        login=login
    )

    return {'Success': True, "balance": balance}

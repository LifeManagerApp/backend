from flask import request
from finance.routs.common import routes
from finance.routs.categories.categories import CategoriesAuth
from flask_jwt_extended import jwt_required, get_jwt_identity


@routes.route('/categories', methods=['POST', 'GET'])
@jwt_required()
def categories():
    login = get_jwt_identity()
    if request.method == 'POST':
        data = request.get_json()
        category_name = data.get('category_name')
        color = data.get('color')

        success = CategoriesAuth.set_categories(category_name=category_name, color=color, login=login)

        return {"success": success}

    elif request.method == 'GET':
        current_user = get_jwt_identity()
        return CategoriesAuth.get_categories(current_user=current_user)



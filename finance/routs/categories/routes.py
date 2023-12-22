from flask import request
from finance.routs.common import routes
from finance.models.models import User, Categories, db
from finance.routs.categories.categories import CategoriesAuth


@routes.route('/categories', methods=['POST', 'GET'])
def categories():

    if request.method == 'POST':
        data = request.get_json()
        category_name = data.get('category_name')
        color = data.get('color')
        user_id = data.get('user_id')

        return CategoriesAuth.set_categories(category_name=category_name, color=color, user_id=user_id)

    elif request.method == 'GET':
        return CategoriesAuth.get_categories()



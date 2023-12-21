from flask import request

from finance.routs.common import routes

from finance.models.models import User, Categories, db


@routes.route('/categories', methods=['POST', 'GET'])
def categories():
    if request.method == 'POST':
        data = request.get_json()
        category_name = data.get('category_name')
        color = data.get('color')
        budget_type = data.get('budget_type')
        try:
            categories = Categories(category_name=category_name, color=color, budget_type=budget_type)
            db.session.add(categories)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)
            return {'success': False}
        return {'success': True}

    elif request.method == 'GET':
        all_categories = {"categories":[]}

        query_set = Categories.query.all()
        for category in query_set:
            temp = {"id":category.id, "category_name":category.category_name, "color":category.color, "budget_type":category.budget_type}
            all_categories["categories"].append(temp)

        return all_categories


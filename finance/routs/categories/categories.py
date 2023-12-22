from finance.models.models import db, Categories, UsersCategory


class CategoriesAuth:

    @staticmethod
    def set_categories(category_name, color, user_id):
        category = Categories.query.filter_by(category_name=category_name, color=color).first()

        if not category:

            try:
                category = Categories(category_name=category_name, color=color)

                db.session.add(category)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(e)
                return False
        user_category = UsersCategory(category.id, user_id)
        user_category.query.filter_by(category_id=category.id, user_id=user_id)

        return True

    @staticmethod
    def get_categories():
        all_categories = {"categories": []}

        query_set = Categories.query.all()
        for category in query_set:
            temp = {"id": category.id, "category_name": category.category_name, "color": category.color}
            all_categories["categories"].append(temp)

        return all_categories


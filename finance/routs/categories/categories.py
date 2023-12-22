from finance.models.models import db, Categories, UsersCategory, User


class CategoriesAuth:

    @staticmethod
    def set_categories(category_name, color, current_user):
        user = User.query.filter_by(login=current_user).first()
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

        user_category = UsersCategory.query.filter_by(category_id=category.id, user_id=user.id).first()
        if not user_category:
            try:
                user_category = UsersCategory(category_id=category.id, user_id=user.id)
                db.session.add(user_category)
                db.session.commit()

            except:
                db.session.rollback()
                return False

        return True

    @staticmethod
    def get_categories():
        all_categories = {"categories": []}

        query_set = Categories.query.all()
        for category in query_set:
            temp = {"id": category.id, "category_name": category.category_name, "color": category.color}
            all_categories["categories"].append(temp)

        return all_categories


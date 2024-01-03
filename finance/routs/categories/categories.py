from finance.models.models import db, Categories, UsersCategory, User
from finance.routs.auth.auth import Auth


class CategoriesAuth:

    @staticmethod
    def set_categories(category_name, color, login):
        user = Auth.get_user(login)
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
    def get_categories(current_user):
        all_categories = {"categories": []}
        user_categories = db.session.query(Categories). \
            join(UsersCategory, Categories.id == UsersCategory.category_id). \
            join(User, UsersCategory.user_id == User.id). \
            filter(User.login == current_user).all()
        for category in user_categories:
            temp = {"id": category.id, "category_name": category.category_name, "color": category.color}
            all_categories["categories"].append(temp)

        return all_categories


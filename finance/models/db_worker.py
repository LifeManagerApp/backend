from finance.models.models import db

class DBWorker:

    def write(self, model_object: db.Model) -> bool:
        try:
            db.session.add(model_object)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)
            return False
        return True


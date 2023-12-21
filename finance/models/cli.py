from app.app import app
from finance.models.models import db


def create_db():
    with app.app_context():
        db.create_all()

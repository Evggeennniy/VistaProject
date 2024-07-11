from flask_sqlalchemy import SQLAlchemy
from app.app import app

db = SQLAlchemy(app)


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    icon = db.Column(db.String(128), nullable=False)
    title = db.Column(db.String(32), nullable=False)

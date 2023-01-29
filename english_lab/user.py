from flask_login import UserMixin

from .instances import database


class User(UserMixin, database.Model):
    """Basic user in database."""
    user_id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(255), nullable=False)
    surname = database.Column(database.String(255), nullable=False)
    email = database.Column(database.String(255), nullable=True, unique=True)

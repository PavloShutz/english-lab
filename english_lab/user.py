"""Module describes basic model for user in database."""


from flask_login import UserMixin

from .instances import database


class User(UserMixin, database.Model):
    """Basic user in database."""

    __tablename__ = 'users'
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(255), nullable=False)
    surname = database.Column(database.String(255), nullable=False)
    email = database.Column(database.String(255), nullable=False, unique=True)
    password = database.Column(database.String(255), nullable=False)

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

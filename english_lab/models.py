"""All models for SQLAlchemy database tool."""


from flask_login import UserMixin
from sqlalchemy.orm import relationship

from .instances import database


class User(UserMixin, database.Model):
    """Basic user in database."""

    __tablename__ = 'users'
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(255), nullable=False)
    surname = database.Column(database.String(255), nullable=False)
    email = database.Column(database.String(255), nullable=False, unique=True)
    password = database.Column(database.String(255), nullable=False)

    def __init__(
            self,
            name: str,
            surname: str,
            email: str,
            password: str
    ) -> None:
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password


class Topic(database.Model):
    """Topic that can be created by admin."""

    __tablename__ = 'topics'
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(255), nullable=False)
    body = database.Column(database.Text, nullable=False)
    questions = relationship("Question", cascade="all, delete", backref="parent")

    def __init__(self, title: str, body: str) -> None:
        self.title = title
        self.body = body


class Question(database.Model):
    """Question to the topic"""
    __tablename__ = 'questions'
    id = database.Column(database.Integer, primary_key=True)
    body = database.Column(database.String(255), nullable=False)
    answer = database.Column(database.String(255), nullable=False)
    topic_id = database.Column(database.Integer, database.ForeignKey("topics.id"))

    def __init__(self, body: str, answer: str, topic_id: int) -> None:
        self.body = body
        self.answer = answer
        self.topic_id = topic_id

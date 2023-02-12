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
    ):
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
    questions = relationship("Question", cascade="all, delete")

    def __init__(self, title: str, body: str):
        self.title = title
        self.body = body


class Question(database.Model):
    """Question to the topic"""
    __tablename__ = 'questions'
    id = database.Column(database.Integer, primary_key=True)
    body = database.Column(database.String(255), nullable=False)
    answers = relationship("Answer", cascade="all, delete")
    topic_id = database.Column(database.Integer, database.ForeignKey("topics.id"))


class Answer(database.Model):
    """Answers to the question."""
    __tablename__ = 'answers'
    id = database.Column(database.Integer, primary_key=True)
    body = database.Column(database.Text, nullable=False)
    question_id = database.Column(database.Integer, database.ForeignKey("questions.id"))

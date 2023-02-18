"""Module for working with database."""


from typing import Optional

from english_lab.instances import database
from english_lab.models import Topic, Question


def add_new_object_to_db(obj) -> None:
    """Add new model to the database."""
    database.session.add(obj)
    database.session.commit()


def get_topic(topic_id: int) -> Optional[Topic]:
    """Get the topic by topic's id."""
    return Topic.query.get(topic_id)


def get_question(topic_id) -> Optional[Question]:
    """Get the question by topic's id."""
    return database.one_or_404(database.select(Question).filter_by(topic_id=topic_id))

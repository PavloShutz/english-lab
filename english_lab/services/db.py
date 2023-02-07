"""Module for working with database."""


from typing import Optional

from english_lab.instances import database
from english_lab.models import Topic


def add_new_object_to_db(obj) -> None:
    """Add new model to the database."""
    database.session.add(obj)
    database.session.commit()


def get_topic(topic_id: int) -> Optional[Topic]:
    """Get the topic by topic's id."""
    return Topic.query.get(topic_id)

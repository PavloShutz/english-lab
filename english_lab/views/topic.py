"""Routes for accessing topic reading."""


from flask import Blueprint, render_template
from flask_login import login_required

from english_lab.services.db import get_topic, get_questions


__all__ = ["topic_bp"]


topic_bp = Blueprint(name="topic", import_name=__name__, url_prefix='/topic')


@topic_bp.get("/read/<int:topic_id>")
@login_required
def read_topic(topic_id) -> str:
    """Render a page with all topic's content."""
    topic = get_topic(topic_id)
    return render_template("topic/topic.html", topic=topic)


@topic_bp.get("/questions/<int:topic_id>")
@login_required
def questions(topic_id) -> str:
    """Render web-page with question for the specific topic"""
    topic_questions = get_questions(topic_id)
    return render_template("topic/questions.html", topic_questions=topic_questions)

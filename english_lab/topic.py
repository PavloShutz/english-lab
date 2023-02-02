"""Routes for accessing topic reading."""


from typing import Union

from flask import Blueprint, render_template, Response
from flask_login import login_required

from .models import Topic

topic_bp = Blueprint(name="topic", import_name=__name__, url_prefix='/topic')


@topic_bp.get("/read/<int:topic_id>")
@login_required
def read_topic(topic_id) -> str:
    """Render a page with all topic's content."""
    topic = Topic.query.get(topic_id)
    return render_template("topic/topic.html", topic=topic)

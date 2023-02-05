"""Routes for accessing topic reading."""


from flask import Blueprint, render_template
from flask_login import login_required

from english_lab.models import Topic


__all__ = ["topic_bp"]


topic_bp = Blueprint(name="topic", import_name=__name__, url_prefix='/topic')


@topic_bp.get("/read/<int:topic_id>")
@login_required
def read_topic(topic_id) -> str:
    """Render a page with all topic's content."""
    topic = Topic.query.get(topic_id)
    return render_template("topic/topic.html", topic=topic)

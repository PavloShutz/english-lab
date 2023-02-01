from typing import Union

from flask import Blueprint, render_template, redirect, url_for, Response
from flask_login import login_required

from .forms import NewTopicForm
from .instances import database
from .models import Topic

topic_bp = Blueprint(name="topic", import_name=__name__, url_prefix='/topic')


@topic_bp.get("/read/<int:topic_id>")
@login_required
def read_topic(topic_id) -> Union[str, Response]:
    topic = Topic.query.get(topic_id)
    return render_template("topic/topic.html", topic=topic)

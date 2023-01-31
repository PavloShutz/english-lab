from typing import Union

from flask import Blueprint, render_template, redirect, url_for, Response
from flask_login import login_required

from .forms import NewTopicForm
from .instances import database
from .models import Topic

topic_editor = Blueprint(name="topic_editor", import_name=__name__, url_prefix='/topic_editor')


@topic_editor.get('/')
def index() -> str:
    """Render main page."""
    topics = Topic.query.all()
    return render_template("index.html", topics=topics)


@topic_editor.route('/create_topic', methods=("GET", "POST"))
@login_required
def create_topic() -> Union[str, Response]:
    form = NewTopicForm()
    if form.validate_on_submit():
        new_topic = Topic(title=form.title.data, body=form.body.data)
        database.session.add(new_topic)
        database.session.commit()
        return redirect(url_for('index'))
    return render_template("topic_editor/create_topic.html", form=form)

from typing import Union

from flask import Blueprint, render_template, redirect, url_for, Response
from flask_login import login_required

from english_lab.forms import NewTopicForm
from english_lab.instances import database
from english_lab.models import Topic
from english_lab.services.admin import admin_required


__all__ = ["topic_editor"]


topic_editor = Blueprint(name="topic_editor", import_name=__name__, url_prefix='/topic_editor')


@topic_editor.route('/create_topic', methods=("GET", "POST"))
@login_required
@admin_required
def create_topic() -> Union[str, Response]:
    form = NewTopicForm()
    if form.validate_on_submit():
        new_topic = Topic(title=form.title.data, body=form.body.data)
        database.session.add(new_topic)
        database.session.commit()
        return redirect(url_for('index'))
    return render_template("topic_editor/create_topic.html", form=form)

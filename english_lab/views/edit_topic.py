from datetime import date
from typing import Union

from flask import Blueprint, render_template, redirect, url_for, Response
from flask_login import login_required
import requests

from english_lab.forms import NewTopicForm, TopicEditForm
from english_lab.instances import database
from english_lab.models import Topic
from english_lab.services.admin import admin_required
from english_lab.services.db import get_topic
from english_lab.services.constants import CHAT_ID, TOKEN


__all__ = ["topic_editor"]


topic_editor = Blueprint(name="topic_editor", import_name=__name__, url_prefix='/topic_editor')


def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    requests.post(url)


@topic_editor.route('/create_topic', methods=("GET", "POST"))
@login_required
@admin_required
def create_topic() -> Union[str, Response]:
    form = NewTopicForm()
    if form.validate_on_submit():
        new_topic = Topic(title=form.title.data, body=form.body.data)
        database.session.add(new_topic)
        database.session.commit()
        send_message(
            f"""
📢 NEW TOPIC IS HERE!

{new_topic.title}

📆 Added: {date.today()}

🔎 Check it on our web-site:

{f'http://127.0.0.1:5000/{url_for("topic.read_topic", topic_id=new_topic.id)}'}
            """
        )
        return redirect(url_for('home.index'))
    return render_template("topic_editor/create_topic.html", form=form)


@topic_editor.route("/edit_topic/<int:topic_id>", methods=("GET", "POST"))
@login_required
@admin_required
def edit_topic(topic_id):
    topic = get_topic(topic_id)
    form = TopicEditForm(title=topic.title, body=topic.body)
    if form.validate_on_submit():
        if form.delete.data:
            database.session.query(Topic).filter(Topic.id == topic_id).delete(synchronize_session=False)
            database.session.commit()
            return redirect(url_for("home.index"))
        elif form.submit.data:
            database.session.query(Topic).filter(Topic.id == topic_id).update(
                {Topic.title: form.title.data, Topic.body: form.body.data},
                synchronize_session=False
            )
            database.session.commit()
            return redirect(url_for("home.index"))
    return render_template("topic_editor/edit_topic.html", topic=topic, form=form)

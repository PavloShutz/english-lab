"""Describing views for editing topics."""


from typing import Union

from flask import Blueprint, render_template, redirect, url_for, Response
from flask_login import login_required

from english_lab.forms import NewTopicForm, TopicEditForm, QuestionForTopicForm
from english_lab.instances import database
from english_lab.models import Topic, Question
from english_lab.services.admin import admin_required
from english_lab.services.db import get_topic, add_new_object_to_db
from english_lab.services.constants import CHAT_ID, TOKEN
from english_lab.services.bot import send_notification_about_new_topic


__all__ = ["topic_editor"]


topic_editor = Blueprint(name="topic_editor", import_name=__name__, url_prefix='/topic_editor')


@topic_editor.route('/create_topic', methods=("GET", "POST"))
@login_required
@admin_required
def create_topic() -> Union[str, Response]:
    """View for creating new topic."""
    form = NewTopicForm()
    if form.validate_on_submit():
        new_topic = Topic(title=form.title.data, body=form.body.data)
        add_new_object_to_db(new_topic)
        send_notification_about_new_topic(TOKEN, CHAT_ID, new_topic)
        return redirect(url_for('home.index'))
    return render_template("topic_editor/create_topic.html", form=form)


@topic_editor.route("/edit_topic/<int:topic_id>", methods=("GET", "POST"))
@login_required
@admin_required
def edit_topic(topic_id):
    """View for editing or deleting existing topic."""
    topic = get_topic(topic_id)
    form = TopicEditForm(title=topic.title, body=topic.body)
    if form.validate_on_submit():
        if form.delete.data:
            database.session.query(Question).filter(Question.topic_id == topic_id).delete(synchronize_session=False)
            database.session.query(Topic).filter(Topic.id == topic_id).delete(synchronize_session=False)
            database.session.commit()
        elif form.new_question.data:
            return redirect(url_for("topic_editor.add_question_for_topic", topic_id=topic_id))
        elif form.submit.data:
            database.session.query(Topic).filter(Topic.id == topic_id).update(
                {Topic.title: form.title.data, Topic.body: form.body.data},
                synchronize_session=False
            )
            database.session.commit()
        return redirect(url_for("home.index"))
    return render_template("topic_editor/edit_topic.html", topic=topic, form=form)


@topic_editor.route("/add_question/<int:topic_id>", methods=("GET", "POST"))
@login_required
@admin_required
def add_question_for_topic(topic_id) -> Union[str, Response]:
    form = QuestionForTopicForm()
    if form.validate_on_submit():
        question = Question(
            body=form.body.data,
            answer=form.answer.data,
            topic_id=topic_id
        )
        add_new_object_to_db(question)
        return redirect(url_for("topic_editor.edit_topic", topic_id=topic_id))
    return render_template("topic_editor/add_question.html", form=form)

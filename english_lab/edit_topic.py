from flask import Blueprint, render_template
from flask_login import login_required


topic_editor = Blueprint(name="topic_editor", import_name=__name__, url_prefix='/topic_editor')


@topic_editor.route('/create_topic', methods=("GET", "POST"))
@login_required
def create_topic() -> str:
    return render_template("topic_editor/create_topic.html")

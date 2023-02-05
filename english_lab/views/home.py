from typing import Union

from flask import Blueprint, render_template, Response

from english_lab.models import Topic


__all__ = ["home"]


home = Blueprint(name="home", import_name=__name__)


@home.get('/')
def index() -> Union[str, Response]:
    """Render main page."""
    topics = Topic.query.all()
    return render_template("home/index.html", topics=topics)

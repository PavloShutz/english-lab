from typing import Union

from flask import Blueprint, render_template, Response

from english_lab.models import Topic
from english_lab.instances import database


__all__ = ["home"]


home = Blueprint(name="home", import_name=__name__)


@home.get('/')
def index() -> Union[str, Response]:
    """Render main page."""
    topics = database.paginate(database.select(Topic), per_page=2, error_out=False)
    return render_template("home/index.html", topics=topics)

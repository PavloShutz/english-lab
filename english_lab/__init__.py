"""Initializing application factory."""

import secrets

from flask import Flask

from .auth import auth
from .account import account
from .constants import ADMINS
from .edit_topic import topic_editor, index
from .instances import (
    database,
    login_manager,
    migrate,
    bootstrap5,
    csrf
)
from .topic import topic_bp


def __initialize_app(app: Flask) -> None:
    """Initialize the application.
    :returns: None
    """
    database.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, database)
    bootstrap5.init_app(app)
    csrf.init_app(app)


def __register_blueprints(app: Flask, *blueprints) -> None:
    """Register all the application blueprints.
    :returns: None
    """
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def create_app() -> Flask:
    """Create and configure the app.
    :returns: Flask object
    """
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///english_lab.db"
    # good themes: flatly, zephyr, lux, minty, sandstone, simplex, sketchy, yeti, united
    app.config["BOOTSTRAP_BOOTSWATCH_THEME"] = 'cosmo'
    app.config["ADMINS"] = ADMINS
    app.secret_key = secrets.token_hex(16)
    __initialize_app(app)
    __register_blueprints(app, auth, account, topic_bp, topic_editor)
    app.add_url_rule('/', view_func=index)

    return app

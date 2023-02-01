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
    """Initialize the application."""
    database.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, database)
    bootstrap5.init_app(app)
    csrf.init_app(app)


def create_app():
    """Create and configure the app."""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///english_lab.db"
    # good themes: flatly, zephyr, lux, minty, sandstone, simplex, sketchy, yeti
    app.config["BOOTSTRAP_BOOTSWATCH_THEME"] = 'yeti'
    app.config["ADMINS"] = ADMINS
    app.secret_key = secrets.token_hex(16)
    __initialize_app(app)
    app.register_blueprint(auth)
    app.register_blueprint(account)
    app.register_blueprint(topic_bp)
    app.register_blueprint(topic_editor)
    app.add_url_rule('/', view_func=index)

    return app

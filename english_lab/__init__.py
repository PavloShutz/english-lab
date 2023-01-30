"""Initializing application factory."""

import secrets

from flask import Flask

from .instances import database, login_manager, migrate, bootstrap5, csrf
from .auth import index, auth


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
    app.secret_key = secrets.token_hex(16)
    __initialize_app(app)
    app.register_blueprint(auth)
    app.add_url_rule('/', view_func=index)

    return app

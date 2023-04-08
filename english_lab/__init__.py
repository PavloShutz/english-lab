"""Initializing application factory."""

import secrets
from datetime import timedelta

from flask import Flask
from flask import request, url_for, redirect, flash


from .instances import (
    database,
    login_manager,
    migrate,
    bootstrap5,
    csrf
)
from .services.constants import ADMINS
from .views import (
    auth,
    account,
    topic_bp,
    topic_editor,
    home,
)


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
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=1)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///english_lab.db"
    # good themes: flatly, zephyr, minty, sandstone, simplex, sketchy, yeti, united
    app.config["BOOTSTRAP_BOOTSWATCH_THEME"] = 'sandstone'
    app.config["ADMINS"] = ADMINS
    __initialize_app(app)
    __register_blueprints(app, auth, account, topic_bp, topic_editor, home)

    @app.route('/change-theme', methods=['POST'])
    def change_theme():
        theme = request.form['theme']
        app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = theme
        flash(f'Theme changed to {theme}.', 'success')
        return redirect(url_for('home.index'))

    return app

"""Initializing application factory."""


from flask import Flask


def create_app(test_config: dict = None):
    """Create and configure the app."""
    app = Flask(__name__)
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    return app

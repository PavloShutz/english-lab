"""Module for admin interface."""


from functools import wraps

from flask import current_app
from flask_login import current_user


def admin_required(func):
    """Decorator for views that can be accessed by admin only."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.email in current_app.config["ADMINS"]:
            return func(*args, **kwargs)
        else:
            return 'Page not found', 404
    return wrapper

"""Routes for user account management."""


from flask import Blueprint, render_template
from flask_login import login_required

from english_lab.models import User


__all__ = ["account"]


account = Blueprint(name="account", import_name=__name__, url_prefix='/account')


@account.get("/profile/<int:user_id>")
@login_required
def profile(user_id) -> str:
    """Show user's profile page.
    :returns: rendered template
    """
    user = User.query.get(user_id)
    return render_template("account/profile.html", user=user)

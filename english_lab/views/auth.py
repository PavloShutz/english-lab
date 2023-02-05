"""Routes for user's authentication."""


from typing import Union

from flask import Blueprint, render_template, flash, redirect, url_for, Response
from flask_login import login_user, login_required, logout_user
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash

from english_lab.services.auth_logic import create_new_user
from english_lab.instances import login_manager, database
from english_lab.models import User
from english_lab.forms import SignUpForm, LoginForm
from english_lab.services.db import add_new_object_to_db


__all__ = ["auth"]


auth = Blueprint(name='auth', import_name=__name__, url_prefix='/auth')


@auth.route('/signup', methods=('GET', 'POST'))
def signup() -> Union[str, Response]:
    """Sign up new user.
    :returns: rendered template or response
    """
    form = SignUpForm()
    if form.validate_on_submit():
        new_user = create_new_user(form)
        try:
            add_new_object_to_db(new_user)
            return redirect(url_for("auth.login"))
        except IntegrityError:
            database.session.rollback()
            flash('There is already user with such email!', 'warning')
    return render_template("auth/signup.html", form=form)


@auth.route('/login', methods=("GET", "POST"))
def login() -> Union[str, Response]:
    """Login existing user.
    :returns: rendered template or response
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for("home.index"))
        flash("Invalid email or password!", 'warning')
    return render_template("auth/login.html", form=form)


@auth.route("/logout")
@login_required
def logout() -> Response:
    """Logout existing user.
    :returns: response
    """
    logout_user()
    return redirect(url_for("home.index"))


@login_manager.user_loader
def load_user(user_id) -> User:
    """Load user by user's id.
    :returns: user
    """
    return User.query.get(user_id)

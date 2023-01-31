"""Routes for user's authentication."""


from typing import Union

from flask import Blueprint, render_template, flash, redirect, url_for, Response
from flask_login import login_user, login_required, logout_user
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash

from .auth_logic import (
    _get_data_from_sign_up_form,
    _create_new_user
)
from .instances import login_manager, database
from .models import User
from .forms import SignUpForm, LoginForm

auth = Blueprint(name='auth', import_name=__name__, url_prefix='/auth')


@auth.route('/signup', methods=('GET', 'POST'))
def signup() -> Union[str, Response]:
    """Sign up new user."""
    form = SignUpForm()
    if form.validate_on_submit():
        new_user = _create_new_user(*_get_data_from_sign_up_form(form))
        try:
            database.session.add(new_user)
            database.session.commit()
            return redirect(url_for("login"))
        except IntegrityError:
            database.session.rollback()
            flash('There is already user with such email!', 'warning')
    return render_template("signup.html", form=form)


@auth.route('/login', methods=("GET", "POST"))
def login() -> Union[str, Response]:
    """Login existing user."""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for("index"))
        flash("Invalid email or password!", 'warning')
    return render_template("login.html", form=form)


@auth.route("/logout")
@login_required
def logout() -> Response:
    """Logout existing user."""
    logout_user()
    return redirect(url_for("index"))


@login_manager.user_loader
def load_user(user_id) -> User:
    """Load user by user's id."""
    return User.query.get(user_id)

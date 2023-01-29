from flask import Blueprint, render_template

from .instances import login_manager
from .user import User
from .forms import SignUpForm

auth = Blueprint(name='auth', import_name=__name__, url_prefix='/auth')


@auth.route('/')
def index() -> str:
    return render_template("index.html")


@auth.route('/signup', methods=('GET', 'POST'))
def signup():
    form = SignUpForm()
    return render_template("signup.html", form=form)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

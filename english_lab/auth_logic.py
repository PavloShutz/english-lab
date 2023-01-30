from werkzeug.security import generate_password_hash

from .forms import SignUpForm
from.user import User


def _get_data_from_sign_up_form(form: SignUpForm) -> tuple:
    name = form.name.data
    surname = form.surname.data
    email = form.email.data
    password = form.password.data
    return name, surname, email, password


def _create_new_user(name, surname, email, password) -> User:
    """Create new user to add to database."""
    return User(
        name=name,
        surname=surname,
        email=email,
        password=generate_password_hash(password)
    )

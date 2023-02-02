"""Business logic for user's authentication"""


from werkzeug.security import generate_password_hash

from .forms import SignUpForm
from.models import User


def _get_data_from_sign_up_form(form: SignUpForm) -> tuple:
    """Get data from user's sign up form.
    :param: form: sign up form for user
    :returns: tuple (name, surname, email and password)
    """
    name = form.name.data
    surname = form.surname.data
    email = form.email.data
    password = form.password.data
    return name, surname, email, password


def _create_new_user(name: str, surname: str, email: str, password: str) -> User:
    """Create new user to add to database."""
    return User(
        name=name,
        surname=surname,
        email=email,
        password=generate_password_hash(password)
    )

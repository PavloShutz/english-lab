"""All forms here."""


from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    EmailField,
    PasswordField,
    SubmitField,
    BooleanField,
    TextAreaField
)
from wtforms.validators import InputRequired, Email, EqualTo, Optional, Length


class SignUpForm(FlaskForm):
    """Form to sign up new user."""
    name = StringField("Name", validators=[InputRequired("Please, enter your name!")])
    surname = StringField("Surname", validators=[InputRequired("Please, enter your surname!")])
    email = EmailField("Email", validators=[InputRequired("Please, enter your email!"), Email()])
    password = PasswordField("Password", validators=[
        InputRequired("Please, enter password!"),
        EqualTo("confirm_password", message="Passwords must match")
    ])
    confirm_password = PasswordField(
        "Confirm password",
        validators=[InputRequired("Please, confirm your password!")]
    )
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    """Login form for signed-up users."""
    email = EmailField("Email", validators=[InputRequired("Please, enter your email!"), Email()])
    password = PasswordField("Password", validators=[InputRequired("Please, enter your password!")])
    remember_me = BooleanField("Remember me", validators=[Optional()])
    submit = SubmitField("Sign Up")


class NewTopicForm(FlaskForm):
    title = StringField("Title", validators=[
        InputRequired("Please, provide title here."),
        Length(min=5)
    ])
    body = TextAreaField("Body", validators=[
        InputRequired("Please, fill body section"),
        Length(min=20)
    ])
    submit = SubmitField("Create new topic")

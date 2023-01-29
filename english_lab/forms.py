from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo


class SignUpForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired("Please, enter your name!")])
    surname = StringField("Surname", validators=[InputRequired("Please, enter your surname!")])
    email = EmailField("Email", validators=[InputRequired("Please, enter your email!"), Email()])
    password = PasswordField("Password", validators=[InputRequired("Please, enter password!")])
    confirm_password = PasswordField(
        "Confirm password",
        validators=[
            InputRequired("Please, confirm your password!"),
            EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

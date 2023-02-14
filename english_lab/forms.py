"""All forms here."""

from flask_bootstrap import SwitchField
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    EmailField,
    PasswordField,
    SubmitField,
    TextAreaField,
    FieldList
)
from wtforms.validators import InputRequired, Email, EqualTo, Optional, Length


class SignUpForm(FlaskForm):
    """Form to sign up new user."""
    name = StringField("🖊 Name", validators=[InputRequired("Please, enter your name!")])
    surname = StringField("🖊 Surname", validators=[InputRequired("Please, enter your surname!")])
    email = EmailField("📧 Email (required)", validators=[InputRequired("Please, enter your email!"), Email()])
    password = PasswordField("🔑 Password (required)", validators=[
        InputRequired("Please, enter password!"),
        EqualTo("confirm_password", message="Passwords must match")
    ])
    confirm_password = PasswordField(
        "🔐 Confirm password (required)",
        validators=[InputRequired("Please, confirm your password!")]
    )
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    """Login form for signed-up users."""
    email = EmailField("📧 Email (required)", validators=[InputRequired("Please, enter your email!"), Email()])
    password = PasswordField("🔑 Password (required)", validators=[InputRequired("Please, enter your password!")])
    remember_me = SwitchField(
        "Remember me",
        validators=[
            Optional()
        ])
    submit = SubmitField("Log In")


class NewTopicForm(FlaskForm):
    """Form for creating new topics."""
    title = StringField("📝 Title", validators=[
        InputRequired("Please, provide title here."),
        Length(min=5)
    ])
    body = TextAreaField("✏ Body",
                         validators=[
                             InputRequired("Please, fill body section"),
                             Length(min=20)
                         ],
                         render_kw={'style': 'height: 360px;'})
    submit = SubmitField("Create new topic")


class TopicEditForm(FlaskForm):
    """Form for editing existing topic."""
    title = StringField("📝 Title", validators=[
        InputRequired("Please, provide title here."),
        Length(min=5)
    ])
    body = TextAreaField("✏ Body",
                         validators=[
                             InputRequired("Please, fill body section"),
                             Length(min=20)
                         ],
                         render_kw={'style': 'height: 360px;'})
    submit = SubmitField("Save changes")
    delete = SubmitField("🗑", render_kw={'class': 'btn-danger'})


class BugReportForm(FlaskForm):
    title = StringField("Problem", validators=[InputRequired()])
    body = TextAreaField("Describe this problem", validators=[InputRequired(), Length(min=15)])
    report = SubmitField("Report")


class QuestionForTopicForm(FlaskForm):
    body = StringField("Question", validators=[InputRequired()])
    answer = StringField("Answer", validators=[InputRequired()])
    submit = SubmitField()

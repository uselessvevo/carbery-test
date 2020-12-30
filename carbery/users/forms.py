from flask_wtf import FlaskForm
from wtforms.fields import (
    PasswordField,
    SubmitField, StringField,
)
from wtforms.validators import EqualTo, InputRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Log in')

    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(LoginForm, self).__init__(*args, **kwargs)


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('password2', 'Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[InputRequired()])
    submit = SubmitField('Register')

    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(RegistrationForm, self).__init__(*args, **kwargs)

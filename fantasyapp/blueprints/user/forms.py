from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Optional, Regexp
from wtforms_components import EmailField, Email, Unique
from lib.util_wtforms import ModelForm
from fantasyapp.blueprints.user.models import User, db
from fantasyapp.blueprints.user.validations import ensure_identity_exists, \
    ensure_existing_password_matches


class LoginForm(FlaskForm):
    # next = HiddenField() redirects user to protected area after logging in
    next = HiddenField()
    identity = StringField('', [DataRequired(), Length(3, 254)])
    password = PasswordField('', [DataRequired(), Length(8, 128)])
    # remember = BooleanField('Stay signed in')


class BeginPasswordResetForm(FlaskForm):
    identity = StringField('',
                           [DataRequired(),
                            Length(3, 254),
                            ensure_identity_exists])


class PasswordResetForm(FlaskForm):
    reset_token = HiddenField()
    password = PasswordField('', [DataRequired(), Length(8, 128)])


class SignupForm(ModelForm):
    email = EmailField('',
                       validators=[
                          DataRequired(),
                          Email(),
                          Unique(User.email,
                                 get_session=lambda: db.session)
                          ])
    password = PasswordField('', [DataRequired(), Length(8, 128)])


class WelcomeForm(ModelForm):
    username_message = 'Letters, numbers and underscores only please.'

    username = StringField('',
                           validators=[
                              Unique(User.username,
                                     get_session=lambda: db.session),
                              DataRequired(),
                              Length(1, 16),
                              Regexp('^\w+$', message=username_message)
                            ])


class UpdateCredentials(ModelForm):
    current_password = PasswordField('',
                                     [DataRequired(),
                                      Length(8, 128),
                                      ensure_existing_password_matches])

    email = EmailField('',
                       validators=[
                          Email(),
                          Unique(User.email,
                                 get_session=lambda: db.session)
                          ])
    password = PasswordField('', [Optional(), Length(8, 128)])

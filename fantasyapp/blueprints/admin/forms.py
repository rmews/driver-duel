from collections import OrderedDict

from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Optional, Regexp, NumberRange, InputRequired
from wtforms_components import Unique

from lib.util_wtforms import ModelForm, choices_from_dict
from fantasyapp.blueprints.user.models import db, User


class SearchForm(FlaskForm):
    q = StringField('Search terms', [Optional(), Length(1, 256)])


class BulkDeleteForm(FlaskForm):
    SCOPE = OrderedDict([
        ('all_selected_items', 'All selected items'),
        ('all_search_results', 'All search results')
    ])

    scope = SelectField('Privileges', [DataRequired()],
                        choices=choices_from_dict(SCOPE, prepend_blank=False))


class UserForm(ModelForm):
    username_message = 'Letters, numbers and underscores only please.'

    username = StringField(validators=[
        Unique(
            User.username,
            get_session=lambda: db.session
        ),
        Optional(),
        Length(1, 16),
        Regexp('^\w+$', message=username_message)
    ])

    role = SelectField('Privileges', [DataRequired()],
                       choices=choices_from_dict(User.ROLE,
                                                 prepend_blank=False))
    active = BooleanField('Yes, allow this user to sign in')

class UpdateGameForm(FlaskForm):
    driver = SelectField('Driver', [DataRequired()], coerce=int)
    race = SelectField('Game', [DataRequired()])
    laps_led = IntegerField('Laps Led', [InputRequired(), NumberRange(min=0, max=500)])
    fastest_laps = IntegerField('Fastest Laps', [InputRequired(), NumberRange(min=0, max=500)])
    differential = IntegerField('Differential', [InputRequired(), NumberRange(min=-40, max=40)])
    finish = IntegerField('Finish', [InputRequired(), NumberRange(min=0, max=40)])

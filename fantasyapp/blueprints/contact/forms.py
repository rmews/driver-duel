from flask_wtf import Form
from wtforms import TextAreaField
from wtforms_components import EmailField
from wtforms.validators import DataRequired, Length


class ContactForm(Form):
    email = EmailField('',[DataRequired(), Length(3, 254)])
    message = TextAreaField('',[DataRequired(), Length(1, 8192)])

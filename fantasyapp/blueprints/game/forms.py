from flask_wtf import FlaskForm
from wtforms import SubmitField


class CreateGame(FlaskForm):
    start = SubmitField("Play")

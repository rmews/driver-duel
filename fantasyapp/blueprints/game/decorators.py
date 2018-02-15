from functools import wraps
from flask import flash, redirect
from flask_login import current_user

import datetime
from lib.util_datetime import tzware_datetime

from fantasyapp.blueprints.game.models.game import Game


def inactive_game_required(url='/settings'):
    """
    Redirect a user to a specified location if they have already played.

    :param url: URL to be redirected to if invalid
    :type url: str
    :return: Function
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Current time
            current_time = tzware_datetime()

            # Determine players status
            # Filter out games by current user & by end date
            current_game = Game.query.filter(Game.user_id == current_user.id) \
                                     .filter(Game.end_time >= current_time) \
                                     .count()

            if current_game >= 1:
                flash('Sorry, you cannot draw drivers more than once a race.', 'danger')
                return redirect(url)

            return f(*args, **kwargs)

        return decorated_function

    return decorator

from flask import (
    Blueprint,
    render_template,
    redirect,
    flash,
    request,
    url_for
)

from flask_login import current_user, login_required

import random
from sqlalchemy import func
from lib.util_datetime import tzware_datetime
from fantasyapp.blueprints.game.decorators import inactive_game_required

from fantasyapp.blueprints.game.forms import CreateGame
from fantasyapp.blueprints.game.models.driver import Driver
from fantasyapp.blueprints.game.models.game import Game

game = Blueprint('game', __name__, template_folder='templates',
                 url_prefix='/game')

@login_required
def before_request():
    """ Protect all the game endpoints. """
    pass


@game.route('/play', methods=['GET', 'POST'])
@inactive_game_required()
def play_game():
    current_time = tzware_datetime()

    # Get current race based on current time
    # current_race type: str
    current_race = Game.get_race_by_id(current_time)

    # Guard against an invalid or missing race.
    if current_race is None:
        flash('Sorry, it appears there is not an active race right now.', 'warning')
        return redirect(url_for('user.settings'))

    drivers = []

    # Randomly query two drivers
    random_drivers = Driver.query.filter(Driver.active == True) \
                                 .order_by(func.random()) \
                                 .limit(2)

    # Refactor later to use list comprehension
    for driver in random_drivers:
        drivers.append(driver)

    driver_1 = drivers[0].id
    driver_2 = drivers[1].id

    # Determine player status
    # Filter out games by current user & by start and end dates
    player_started = Game.query.filter(Game.user_id == current_user.id) \
                               .filter((Game.start_time <= current_time) \
                                & (Game.end_time >= current_time)) \
                               .count()

    form = CreateGame()

    if form.validate_on_submit():
        # Set player has started game = True
        player_started = True

        # Get race start and end times by passing race key (str)
        start_time = Game.get_race_start_time(current_race)
        end_time = Game.get_race_end_time(current_race)

        # Set game instance params
        params = {
            'user_id': current_user.id,
            'start_time': start_time,
            'end_time': end_time,
            'race': current_race,
            'player_started': player_started,
            'driver_1': driver_1,
            'driver_2': driver_2
        }

        # Initialize Game instance and save user info
        game = Game(**params)
        game.save_and_update_user(current_user)

    return render_template('game/play.html',
                           drivers=drivers,
                           player_started=player_started,
                           form=form)


@game.route('/confirm', methods=['POST'])
def update_game():

    form = CreateGame()

    if form.validate_on_submit():
        # Pass in the driver id and name
        driver = int(request.args.get('driver_id'))
        driver_name = request.args.get('driver_name')

        # Guard against someone submitting wrong driver
        current_time = tzware_datetime()
        current_race = Game.get_race_by_id(current_time)

        # Get the game object that we want to update
        game_to_update = Game.query.filter(Game.user_id == current_user.id) \
                                   .filter(Game.race == current_race) \
                                   .one()

        if driver not in (int(game_to_update.driver_1), int(game_to_update.driver_2)):
            flash('Sorry, it looks like you tried to submit a driver that was not drawn.', 'warning')
            return redirect(url_for('user.settings'))

        # Save and commit the selected driver to game object
        game_to_update.selected_driver = driver
        game_to_update.save()

        flash('Good luck! You picked %s. Come back after the race to see how you did.' % driver_name, 'success')
        return redirect(url_for('user.settings'))
    else:
        flash('It looks like something went wrong.', 'warning')
        return redirect(url_for('game.dashboard'))


@game.route('/history')
def dashboard():
    # Get all games player has played
    games = Game.query.filter(Game.user_id == current_user.id) \
                      .order_by(Game.end_time.asc()) \
                      .all()

    # Get all drivers
    drivers = Driver.query.all()

    return render_template('game/history.html',
                           games=games,
                           drivers=drivers)

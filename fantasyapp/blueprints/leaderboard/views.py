from flask import (
    Blueprint,
    render_template
)
from lib.util_datetime import tzware_datetime

from fantasyapp.blueprints.leaderboard.models import Leaderboard
from fantasyapp.blueprints.user.models import User

leaderboard = Blueprint('leaderboard', __name__,
                        template_folder='templates',
                        url_prefix='/leaderboard')


@leaderboard.route('')
def season_rank():
    games = Leaderboard.group_games()
    users = User.query.all()

    current_time = tzware_datetime()
    races = Leaderboard.get_active_races(current_time)

    return render_template('leaderboard/index.html',
                           games=games,
                           users=users,
                           races=races)


@leaderboard.route('/races/<int:id>')
def weekly_rank(id):
    game = Leaderboard.group_games_by_week(id)
    users = User.query.all()

    current_time = tzware_datetime()
    races = Leaderboard.get_active_races(current_time)

    return render_template('leaderboard/race_leaders.html',
                           game=game,
                           users=users,
                           races=races)

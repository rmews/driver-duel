from flask import current_app
from sqlalchemy import func

from fantasyapp.blueprints.user.models import db, User
from fantasyapp.blueprints.game.models.game import Game
from fantasyapp.blueprints.game.models.driver import Driver
from config import settings


class Dashboard(object):
    @classmethod
    def group_and_count_users(cls):
        """
        Perform a group by/count on all users.

        :return: dict
        """
        return Dashboard._group_and_count(User, User.role)

    @classmethod
    def group_and_count_races(cls):
        """
        Perform a group by/count on all games.

        :return: dict
        """
        return Dashboard._group_and_count(Game, Game.race)

    @classmethod
    def group_and_count_drivers(cls):
        """
        Perform a group by/count on all drivers.

        :return: dict
        """
        return Dashboard._group_and_count(Driver, Driver.active)

    @classmethod
    def _group_and_count(cls, model, field):
        """
        Group results for a specific model and field.

        :param model: Name of the model
        :type model: SQLAlchemy model
        :param field: Name of the field to group on
        :type field: SQLAlchemy field
        :return: dict
        """
        count = func.count(field)
        query = db.session.query(count, field).group_by(field).all()

        results = {
            'query': query,
            'total': model.query.count()
        }

        return results

    @classmethod
    def calculate_points(cls, laps_led, fastest_laps, differential, finish):
        """
        Calculate the total points for a game.

        :param laps_led: Number of laps led
        :type laps_led: Int
        :param fastest_laps: Number of fastest laps
        :type fastest_laps: Int
        :param differential: Number for differential
        :type differential: Int
        :param finish: Number for finishing position
        :type finish: Int
        :return: float
        """
        points_led = float(laps_led * float(current_app.config['POINTS_LAPS_LEAD'][str('1')]))
        points_fastest_laps = float(fastest_laps * float(current_app.config['POINTS_FASTEST_LAPS'][str('1')]))
        points_differential = float(differential)
        points_finish = float(current_app.config['POINTS_FINISH'][str(finish)])

        return points_led + points_fastest_laps + points_differential + points_finish

from sqlalchemy import func, desc
from config import settings

from fantasyapp.blueprints.game.models.game import db, Game


class Leaderboard(object):
    @classmethod
    def group_games(cls):
        """
        Perform a group on all games by user.

        :return: dict
        """
        return Leaderboard._group(Game.laps_led,
                                  Game.fastest_laps,
                                  Game.differential,
                                  Game.total_points,
                                  Game.user_id)

    @classmethod
    def group_games_by_week(cls, race):
        """
        Find games by race id.

        :param identity: race
        :type identity: str
        :return: Game instance
        """

        return Game.query.filter(Game.race == str(race)).order_by(desc(Game.total_points))

    @classmethod
    def _group(cls, laps_led, fastest_laps, differential, total_points, group_field):
        """
        Group results for a specific model and fields.

        :param laps_led: Name of the field being queried
        :type laps_led: SQLAlchemy field
        :param fastest_laps: Name of the field being queried
        :type fastest_laps: SQLAlchemy field
        :param differential: Name of the field being queried
        :type differential: SQLAlchemy field
        :param total_points: Name of the field being queried
        :type total_points: SQLAlchemy field
        :param group_field: Name of the field to group on
        :type group_field: SQLAlchemy field
        :return: dict
        """
        query = db.session.query(group_field,
                                 func.sum(laps_led).label('laps_led'),
                                 func.sum(fastest_laps).label('fastest_laps'),
                                 func.sum(differential).label('differential'),
                                 func.sum(total_points).label('total_points')) \
                          .group_by(group_field) \
                          .order_by(desc('total_points'))

        return query

    @classmethod
    def get_active_races(cls, current_time):
        """
        Get active races based on the current time.

        :param current_time: current time
        :type current_time: integer
        :return: list
        """
        result = [(key, value['name']) for key, value in sorted(settings.RACES.items()) \
                    if value.get('end_time') <= current_time ]

        return result

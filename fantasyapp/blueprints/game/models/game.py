from lib.util_sqlalchemy import ResourceMixin, AwareDateTime
from lib.util_datetime import tzware_datetime
from fantasyapp.extensions import db
from config import settings
from sqlalchemy import func


class Game(ResourceMixin, db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer,
                   primary_key=True)

    # Relationships.
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id',
                                      onupdate='CASCADE',
                                      ondelete='CASCADE'),
                        index=True,
                        nullable=False)
    selected_driver = db.Column(db.Integer,
                                db.ForeignKey('drivers.id',
                                              onupdate='CASCADE',
                                              ondelete='CASCADE'),
                                index=True,
                                nullable=True)

    # Game details.
    start_time = db.Column(AwareDateTime())
    end_time = db.Column(AwareDateTime())
    race = db.Column(db.String(4))
    player_started = db.Column(db.Boolean(),
                               nullable=False,
                               server_default='0')
    driver_1 = db.Column(db.Integer())
    driver_2 = db.Column(db.Integer())
    laps_led = db.Column(db.Integer())
    fastest_laps = db.Column(db.Integer())
    differential = db.Column(db.Integer())
    finish = db.Column(db.Integer())
    total_points = db.Column(db.Float())

    def __init__(self, **kwargs):
        # Call Flask-SQLAlchemy's constructor.
        super(Game, self).__init__(**kwargs)

    @classmethod
    def get_race_by_id(cls, current_time):
        """
        Pick the race based on the current time.

        :param current_time: current time
        :type current_time: integer
        :return: key or none
        """
        for key, value in settings.RACES.items():
            if value.get('start_time') <= current_time and value.get('end_time') >= current_time:
                return key

        return None

    @classmethod
    def get_race_start_time(cls, current_race):
        """
        Get the race start time based on the current race.

        :param current_race: Current Race id
        :type current_race: str
        :return: utc datetime or None
        """
        for key in settings.RACES.keys():
            if key == current_race:
                return settings.RACES[key]['start_time']

        return None

    @classmethod
    def get_race_end_time(cls, current_race):
        """
        Get the race end time based on the current race.

        :param current_race: Current Race id
        :type current_race: str
        :return: utc datetime or None
        """
        for key in settings.RACES.keys():
            if key == current_race:
                return settings.RACES[key]['end_time']

        return None

    def save_and_update_user(self, user):
        """
        Commit the game and update the user's information.

        :return: SQLAlchemy save result
        """
        self.save()

        user.last_game_on = tzware_datetime()
        return user.save()

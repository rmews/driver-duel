from lib.util_sqlalchemy import ResourceMixin
from lib.util_datetime import tzware_datetime

from fantasyapp.blueprints.game.models.game import Game
from fantasyapp.extensions import db


class Driver(ResourceMixin, db.Model):
    __tablename__ = 'drivers'
    id = db.Column(db.Integer, primary_key=True)

    # Relationships.
    games = db.relationship(Game, backref='games', passive_deletes=True)

    # Driver details.
    name = db.Column(db.String(50), index=True)
    active = db.Column('is_active', db.Boolean(), nullable=False,
                       server_default='1')
    picture = db.Column(db.String(256))

    def __init__(self, **kwargs):
        # Call Flask-SQLAlchemy's constructor.
        super(Driver, self).__init__(**kwargs)

    @classmethod
    def search(cls, query):
        """
        Search a resource by 1 or more fields.

        :param query: Search query
        :type query: str
        :return: SQLAlchemy filter
        """
        if not query:
            return ''

        search_query = '%{0}%'.format(query)
        search_chain = Driver.name.ilike(search_query)

        return search_chain

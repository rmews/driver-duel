import datetime
from datetime import timedelta
import pytz
utc = pytz.utc

DEBUG = True
LOG_LEVEL = 'DEBUG'  # CRITICAL / ERROR / WARNING / INFO / DEBUG

SERVER_NAME = 'localhost:8000'
SECRET_KEY = 'insecurekeyfordev'

# Flask-Mail.
MAIL_DEFAULT_SENDER = 'contact@local.host'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'you@gmail.com'
MAIL_PASSWORD = 'awesomepassword'

# Celery.
CELERY_BROKER_URL = 'redis://:devpassword@redis:6379/0'
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5

# SQLAlchemy.
db_uri = 'postgresql://fantasyapp:devpassword@postgres:5432/fantasyapp'
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

# User.
SEED_ADMIN_EMAIL = 'dev@local.host'
SEED_ADMIN_PASSWORD = 'devpassword'
REMEMBER_COOKIE_DURATION = timedelta(days=90)

# Images.
UPLOAD_FOLDER = 'fantasyapp/static/images/drivers'
IMAGE_URL = 'images/drivers'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# Add Payouts Here Later.
GAME_PAYOUT = {}
LEADERBOARD_PAYOUT = {}

# Game Scoring.
POINTS_FINISH = {
    '1': 40,
    '2': 39,
    '3': 38,
    '4': 37,
    '5': 36,
    '6': 35,
    '7': 34,
    '8': 33,
    '9': 32,
    '10': 31,
    '11': 30,
    '12': 29,
    '13': 28,
    '14': 27,
    '15': 26,
    '16': 25,
    '17': 24,
    '18': 23,
    '19': 22,
    '20': 21,
    '21': 20,
    '22': 19,
    '23': 18,
    '24': 17,
    '25': 16,
    '26': 15,
    '27': 14,
    '28': 13,
    '29': 12,
    '30': 11,
    '31': 10,
    '32': 9,
    '33': 8,
    '34': 7,
    '35': 6,
    '36': 5,
    '37': 4,
    '38': 3,
    '39': 2,
    '40': 1
}

POINTS_LAPS_LEAD = {
    '1': 0.25
}

POINTS_FASTEST_LAPS = {
    '1': 0.5
}

# Races
# Start time needs to be 2 hours at the end of the race leading to the week
# End time needs to be 15 minutes before race starts.
RACES = {
    '1': {
        'id': 'race_4',
        'name': 'Phoenix (Spring)',
        'start_time': datetime.datetime(2018, 3, 5, 4, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 3, 11, 20, 30, 0, tzinfo=utc),
    },
    '2': {
        'id': 'race_5',
        'name': 'Auto Club',
        'start_time': datetime.datetime(2018, 3, 12, 4, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 3, 18, 20, 30, 0, tzinfo=utc),
    },
    '3': {
        'id': 'race_6',
        'name': 'Martinsville (Spring)',
        'start_time': datetime.datetime(2018, 3, 19, 4, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 3, 25, 19, 0, 0, tzinfo=utc),
    },
    '4': {
        'id': 'race_7',
        'name': 'Texas (Spring)',
        'start_time': datetime.datetime(2018, 3, 26, 21, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 4, 8, 19, 0, 0, tzinfo=utc),
    },
    '5': {
        'id': 'race_8',
        'name': 'Bristol (Spring)',
        'start_time': datetime.datetime(2018, 4, 9, 3, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 4, 15, 19, 0, 0, tzinfo=utc),
    },
    '6': {
        'id': 'race_9',
        'name': 'Richmond (Spring)',
        'start_time': datetime.datetime(2018, 4, 17, 3, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 4, 21, 23, 30, 0, tzinfo=utc),
    },
    '7': {
        'id': 'race_10',
        'name': 'Talladega (Spring)',
        'start_time': datetime.datetime(2018, 4, 23, 7, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 4, 29, 19, 0, 0, tzinfo=utc),
    },
    '8': {
        'id': 'race_11',
        'name': 'Dover (Spring)',
        'start_time': datetime.datetime(2018, 5, 1, 3, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 5, 6, 19, 0, 0, tzinfo=utc),
    },
    '9': {
        'id': 'race_12',
        'name': 'Kansas (Spring)',
        'start_time': datetime.datetime(2018, 5, 8, 3, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 5, 13, 1, 0, 0, tzinfo=utc),
    },
    '10': {
        'id': 'race_13',
        'name': 'Charlotte (Spring)',
        'start_time': datetime.datetime(2018, 5, 21, 9, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 5, 27, 23, 0, 0, tzinfo=utc),
    },
    '11': {
        'id': 'race_14',
        'name': 'Pocono (Spring)',
        'start_time': datetime.datetime(2018, 5, 29, 7, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 6, 3, 19, 0, 0, tzinfo=utc),
    },
    '12': {
        'id': 'race_15',
        'name': 'Michigan (Spring)',
        'start_time': datetime.datetime(2018, 6, 5, 3, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 6, 10, 19, 0, 0, tzinfo=utc),
    },
    '13': {
        'id': 'race_16',
        'name': 'Sonoma',
        'start_time': datetime.datetime(2018, 6, 12, 3, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 6, 24, 20, 0, 0, tzinfo=utc),
    },
    '14': {
        'id': 'race_17',
        'name': 'Chicagoland',
        'start_time': datetime.datetime(2018, 6, 26, 4, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 7, 1, 19, 30, 0, tzinfo=utc),
    },
    '15': {
        'id': 'race_18',
        'name': 'Daytona (Summer)',
        'start_time': datetime.datetime(2018, 7, 3, 3, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 7, 8, 0, 0, 0, tzinfo=utc),
    },
    '16': {
        'id': 'race_19',
        'name': 'Kentucky',
        'start_time': datetime.datetime(2018, 7, 9, 8, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 7, 15, 0, 30, 0, tzinfo=utc),
    },
    '17': {
        'id': 'race_20',
        'name': 'New Hampshire (Summer)',
        'start_time': datetime.datetime(2018, 7, 16, 9, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 7, 22, 19, 0, 0, tzinfo=utc),
    },
    '18': {
        'id': 'race_21',
        'name': 'Pocono (Summer)',
        'start_time': datetime.datetime(2018, 7, 24, 3, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 7, 29, 19, 30, 0, tzinfo=utc),
    },
    '19': {
        'id': 'race_22',
        'name': 'Watkins Glen',
        'start_time': datetime.datetime(2018, 7, 31, 3, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 8, 5, 19, 30, 0, tzinfo=utc),
    },
    '20': {
        'id': 'race_23',
        'name': 'Michigan (Summer)',
        'start_time': datetime.datetime(2018, 8, 7, 3, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 8, 12, 19, 30, 0, tzinfo=utc),
    },
    '21': {
        'id': 'race_24',
        'name': 'Bristol (Summer)',
        'start_time': datetime.datetime(2018, 8, 14, 3, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 8, 19, 0, 30, 0, tzinfo=utc),
    },
    '22': {
        'id': 'race_25',
        'name': 'Darlington',
        'start_time': datetime.datetime(2018, 8, 20, 8, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 9, 2, 23, 0, 0, tzinfo=utc),
    },
    '23': {
        'id': 'race_26',
        'name': 'Indianapolis',
        'start_time': datetime.datetime(2018, 9, 4, 7, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 9, 9, 19, 0, 0, tzinfo=utc),
    },
    '24': {
        'id': 'race_27',
        'name': 'Las Vegas (Fall)',
        'start_time': datetime.datetime(2018, 9, 11, 3, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 9, 16, 20, 0, 0, tzinfo=utc),
    },
    '25': {
        'id': 'race_28',
        'name': 'Richmond (Fall)',
        'start_time': datetime.datetime(2018, 9, 18, 4, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 9, 23, 0, 30, 0, tzinfo=utc),
    },
    '26': {
        'id': 'race_29',
        'name': 'Charlotte (Fall)',
        'start_time': datetime.datetime(2018, 9, 24, 8, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 9, 30, 19, 0, 0, tzinfo=utc),
    },
    '27': {
        'id': 'race_30',
        'name': 'Dover (Fall)',
        'start_time': datetime.datetime(2018, 10, 2, 3, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 10, 7, 19, 0, 0, tzinfo=utc),
    },
    '28': {
        'id': 'race_31',
        'name': 'Talladega (Fall)',
        'start_time': datetime.datetime(2018, 10, 9, 3, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 10, 14, 19, 0, 0, tzinfo=utc),
    },
    '29': {
        'id': 'race_32',
        'name': 'Kansas (Fall)',
        'start_time': datetime.datetime(2018, 10, 16, 3, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 10, 21, 19, 0, 0, tzinfo=utc),
    },
    '30': {
        'id': 'race_33',
        'name': 'Martinsville (Fall)',
        'start_time': datetime.datetime(2018, 10, 23, 3, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 10, 28, 19, 30, 0, tzinfo=utc),
    },
    '31': {
        'id': 'race_34',
        'name': 'Texas (Fall)',
        'start_time': datetime.datetime(2018, 10, 30, 3, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 11, 4, 20, 0, 0, tzinfo=utc),
    },
    '32': {
        'id': 'race_35',
        'name': 'Phoenix (Fall)',
        'start_time': datetime.datetime(2018, 11, 6, 4, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 11, 11, 19, 30, 0, tzinfo=utc),
    },
    '33': {
        'id': 'race_36',
        'name': 'Homestead-Miami',
        'start_time': datetime.datetime(2018, 11, 13, 4, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 11, 18, 19, 30, 0, tzinfo=utc),
    }
}

RATELIMIT_STORAGE_URL = CELERY_BROKER_URL
RATELIMIT_STRATEGY = 'fixed-window-elastic-expiry'
RATELIMIT_HEADERS_ENABLED = True

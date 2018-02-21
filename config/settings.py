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
CELERY_RESULT_BACKEND = 'redis://:devpassword@redis:6379/0'
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
        'id': 'race_1',
        'name': 'Daytona 500',
        'start_time': datetime.datetime(2018, 2, 9, 4, 0, tzinfo=utc),
        'end_time': datetime.datetime(2018, 2, 9, 4, 9, 59, tzinfo=utc),
    },
    '2': {
        'id': 'race_2',
        'name': 'Folds of Honor QuikTrip 500',
        'start_time': datetime.datetime(2018, 2, 9, 4, 10, tzinfo=utc),
        'end_time': datetime.datetime(2018, 2, 9, 4, 19, 59, tzinfo=utc),
    },
    '3': {
        'id': 'race_3',
        'name': 'Hello World',
        'start_time': datetime.datetime(2018, 2, 9, 4, 20, tzinfo=utc),
        'end_time': datetime.datetime(2018, 2, 9, 4, 29, 59, tzinfo=utc),
    },
    '4': {
        'id': 'race_4',
        'name': 'Hello World2',
        'start_time': datetime.datetime(2018, 2, 9, 4, 30, tzinfo=utc),
        'end_time': datetime.datetime(2018, 2, 9, 4, 39, 59, tzinfo=utc),
    },
    '5': {
        'id': 'race_5',
        'name': 'Hello World3',
        'start_time': datetime.datetime(2018, 2, 9, 4, 40, tzinfo=utc),
        'end_time': datetime.datetime(2018, 2, 9, 4, 49, 59, tzinfo=utc),
    },
    '6': {
        'id': 'race_6',
        'name': 'Hello World4',
        'start_time': datetime.datetime(2018, 2, 9, 5, 20, tzinfo=utc),
        'end_time': datetime.datetime(2018, 2, 9, 5, 29, 59, tzinfo=utc),
    },
    '7': {
        'id': 'race_7',
        'name': 'Hello World5',
        'start_time': datetime.datetime(2018, 2, 9, 5, 30, tzinfo=utc),
        'end_time': datetime.datetime(2018, 2, 9, 5, 39, 59, tzinfo=utc),
    },
    '8': {
        'id': 'race_8',
        'name': 'Hello World6',
        'start_time': datetime.datetime(2018, 2, 21, 6, 30, tzinfo=utc),
        'end_time': datetime.datetime(2018, 2, 21, 6, 39, 59, tzinfo=utc),
    },

}

# RACES = {
#     '0': {
#         'id': 'race_1',
#         'name': 'Daytona 500',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 00, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 04, 59, tzinfo=utc),
#     },
#     '1': {
#         'id': 'race_2',
#         'name': 'Folds of Honor QuikTrip 500',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 10, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 14, 59, tzinfo=utc),
#     },
#     '2': {
#         'id': 'race_3',
#         'name': 'Pennzoil 400 presented by Jiffy Lube',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '3': {
#         'id': 'race_4',
#         'name': 'TicketGuardian 500',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '4': {
#         'id': 'race_5',
#         'name': 'Auto Club 400',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '5': {
#         'id': 'race_6',
#         'name': 'STP 500',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '6': {
#         'id': 'race_7',
#         'name': 'O'\''Reilly Auto Parts 500',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '7': {
#         'id': 'race_8',
#         'name': 'Food City 500',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '8': {
#         'id': 'race_9',
#         'name': 'Toyota Owners 400',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '9': {
#         'id': 'race_10',
#         'name': 'GEICO 500',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '10': {
#         'id': 'race_11',
#         'name': 'AAA 400 Drive for Autism',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '11': {
#         'id': 'race_12',
#         'name': 'Monster Energy NASCAR Cup Series Race at Kansas',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '12': {
#         'id': 'race_13',
#         'name': 'Coca-Cola 600',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '13': {
#         'id': 'race_14',
#         'name': 'Pocono 400',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '14': {
#         'id': 'race_15',
#         'name': 'FireKeepers Casino 400',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '15': {
#         'id': 'race_16',
#         'name': 'Toyota / Save Mart 350',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '16': {
#         'id': 'race_17',
#         'name': 'Monster Energy NASCAR Cup Series Race at Chicagoland',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '17': {
#         'id': 'race_18',
#         'name': 'Coke Zero 400',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '18': {
#         'id': 'race_19',
#         'name': 'Quaker State 400 Presented by Advance Auto Parts',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '19': {
#         'id': 'race_20',
#         'name': 'New Hampshire 301',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '20': {
#         'id': 'race_21',
#         'name': 'Overton'\''s 400',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '21': {
#         'id': 'race_22',
#         'name': 'GoBowling at The Glen',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '22': {
#         'id': 'race_23',
#         'name': 'Monster Energy NASCAR Cup Series Race at Michigan',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '23': {
#         'id': 'race_24',
#         'name': 'Bass Pro Shops NRA Night Race',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '24': {
#         'id': 'race_25',
#         'name': 'Bojangles'\'' Southern 500',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '25': {
#         'id': 'race_26',
#         'name': 'Big Machine Brickyard 400',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '26': {
#         'id': 'race_27',
#         'name': 'South Point 400',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '27': {
#         'id': 'race_28',
#         'name': 'Federated Auto Parts 400',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '28': {
#         'id': 'race_29',
#         'name': 'Bank of America 500',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '29': {
#         'id': 'race_30',
#         'name': 'Monster Energy NASCAR Cup Series at Dover',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '30': {
#         'id': 'race_31',
#         'name': 'Alabama 500',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '31': {
#         'id': 'race_32',
#         'name': 'Hollywood Casino 400',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '32': {
#         'id': 'race_33',
#         'name': 'First Data 500',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '33': {
#         'id': 'race_34',
#         'name': 'AAA Texas 500',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '34': {
#         'id': 'race_35',
#         'name': 'Can-Am 500',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     },
#     '35': {
#         'id': 'race_36',
#         'name': 'Ford EcoBoost 400',
#         'start_time': datetime.datetime(2018, 2, 6, 5, 15, tzinfo=utc),
#         'end_time': datetime.datetime(2018, 2, 6, 5, 19, 59, tzinfo=utc),
#     }
# }

RATELIMIT_STORAGE_URL = CELERY_BROKER_URL
RATELIMIT_STRATEGY = 'fixed-window-elastic-expiry'
RATELIMIT_HEADERS_ENABLED = True

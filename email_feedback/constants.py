import os
import environ
from os.path import join, dirname, abspath

env = environ.Env()

env.read_env(env.str(
    'ENV_PATH',
    join(dirname(dirname(abspath(__file__))), '.env')
))

SMTP_SERVER_ADDRESS = os.environ.get('SMTP_SERVER_ADDRESS')
PORT = os.environ.get('PORT')
SENDER_PASSWORD = os.environ.get('SENDER_PASSWORD')
SENDER_ADDRESS = os.environ.get('SENDER_ADDRESS')
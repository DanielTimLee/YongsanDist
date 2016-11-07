from flask import Flask

app = Flask(__name__, static_folder='static')
app.config.from_object('config')

COOKIE_KEY_ACCESS_TOKEN = app.config['COOKIE_KEY_ACCESS_TOKEN']
COOKIE_KEY_USER_DATA = app.config['COOKIE_KEY_USER_DATA']

# from flask_wtf import CsrfProtect
#
# CsrfProtect(app)

from app.helpers.util import *
from app.helpers.jinja import *

from app.routes import *

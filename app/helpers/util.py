import ast
import base64

import arrow
from flask import request

from app import app, COOKIE_KEY_USER_DATA


def Validation(form):
    if request.method == 'POST' and form.validate():
        return True

    return False


def bake_userdata(userdata):
    encoded = str(userdata).encode('utf8')
    return base64.b64encode(encoded)


def extract_userdata(cookies):
    decoded = base64.b64decode(cookies[COOKIE_KEY_USER_DATA]).decode('utf8')
    return ast.literal_eval(decoded)


def extract_username(cookies):
    userdata = extract_userdata(cookies)
    return userdata['username']


@app.add_template_filter
def extract_username_from_userdata(cookies):
    userdata = extract_userdata(cookies)
    return userdata['username']


def extract_user_name(cookies):
    userdata = extract_userdata(cookies)
    return userdata['name']


@app.add_template_filter
def extract_user_name_from_userdata(cookies):
    userdata = extract_userdata(cookies)
    return userdata['name']


def extract_user_nickname(cookies):
    userdata = extract_userdata(cookies)
    return userdata['nickname']


@app.add_template_filter
def extract_user_nickname_from_userdata(cookies):
    userdata = extract_userdata(cookies)
    return userdata['nickname']


def extract_user_gender(cookies):
    userdata = extract_userdata(cookies)
    return userdata['gender']


@app.add_template_filter
def extract_user_gender_from_userdata(cookies):
    userdata = extract_userdata(cookies)
    return userdata['gender']


def extract_user_email(cookies):
    userdata = extract_userdata(cookies)
    return userdata['email']


@app.add_template_filter
def extract_user_email_from_userdata(cookies):
    userdata = extract_userdata(cookies)
    return userdata['email']


def extract_user_type(cookies):
    userdata = extract_userdata(cookies)
    return userdata['type']


@app.add_template_filter
def extract_user_type_from_userdata(cookies):
    userdata = extract_userdata(cookies)
    return userdata['type']


def extract_user_company(cookies):
    userdata = extract_userdata(cookies)
    return userdata['company']


@app.add_template_filter
def extract_user_company_from_userdata(cookies):
    userdata = extract_userdata(cookies)
    return userdata['company']


def extract_user_join(cookies):
    userdata = extract_userdata(cookies)
    return userdata['join']


@app.add_template_filter
def extract_user_join_from_userdata(cookies):
    userdata = extract_userdata(cookies)
    return userdata['join']


@app.add_template_filter
def humanize(time):
    now = arrow.utcnow()
    time = arrow.get(time)
    return now.humanize(time, locale='ko')

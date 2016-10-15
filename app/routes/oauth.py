from functools import wraps
from urllib.parse import urlparse, urlencode, parse_qs

from flask import request, redirect, url_for, make_response, render_template

from app import app, COOKIE_KEY_ACCESS_TOKEN, COOKIE_KEY_USER_DATA
from app.helpers.api_request import RequestOauth, RequestUserAPI
from app.helpers.util import bake_userdata


def get_oauth_url():
    params = {
        'client_id': app.config.get('OAUTH_CLIENT_ID'),
        'response_type': 'code',
        'scope': 'god',
        'next': urlparse(request.url).path
    }

    return "{0}/oauth/authorize?{1}".format(app.config.get('OAUTH_API'), urlencode(params))


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if COOKIE_KEY_ACCESS_TOKEN not in request.cookies:
            return redirect(get_oauth_url())
        return f(*args, **kwargs)

    return decorated_function


@app.route('/oauth', methods=['GET'])
def oauth_login():
    form_data = {
        'code': request.args['code'],
        'redirect_uri': url_for('oauth_login', _external=True),
        'grant_type': 'authorization_code',
        'client_id': app.config.get('OAUTH_CLIENT_ID'),
        'client_secret': app.config.get('OAUTH_CLIENT_SECRET'),
        'scope': 'god'
    }

    response = RequestOauth.get_token(form_data)

    oauth_access_token = response['access_token']

    app.logger.info("ACCESS TOKEN: {0}".format(oauth_access_token))

    params = parse_qs(urlparse(request.referrer).query)
    next_url = params['next'][0] if 'next' in params else url_for('index')

    response = make_response(render_template('jump.html', next=next_url))
    response.set_cookie(COOKIE_KEY_ACCESS_TOKEN, oauth_access_token)

    response_userdata = RequestUserAPI.get_user_data(oauth_access_token)
    response.set_cookie(COOKIE_KEY_USER_DATA, bake_userdata(response_userdata))

    return response

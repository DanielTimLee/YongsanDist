from flask import render_template

from app import app
from app.routes.oauth import get_oauth_url


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('pages/index/index.html',
                           signin=get_oauth_url())


@app.route("/about")
def about():
    return render_template('pages/about.html',
                           signin=get_oauth_url())

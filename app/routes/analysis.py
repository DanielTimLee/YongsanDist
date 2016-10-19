from flask import render_template

from app import app
from app.routes.oauth import login_required


@app.route('/analysis/index', methods=['GET', 'POST'])
@login_required
def analysis_index():
    return render_template('pages/analysis/index.html')

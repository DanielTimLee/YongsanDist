from flask import render_template, flash, redirect, url_for

from app import app
from app.forms.project import AddProjectForm
from app.helpers.api_request import RequestProjectAPI
from app.routes.oauth import login_required


@app.route('/project', methods=['GET', 'POST'])
@login_required
def project_list():
    form = AddProjectForm()
    result = RequestProjectAPI.get_project_list()
    lists = result['items']

    if form.validate_on_submit():
        payload = dict(
            title=form.title.data,
            description=form.description.data
        )
        response_data = RequestProjectAPI.add_project(payload)
        flash('성공적으로 프로젝트를 추가했습니다.')
        return redirect(url_for('project_list'))

    elif form.is_submitted():
        flash('프로젝트 추가에 문제가 발생했습니다.')

    return render_template('pages/project/list.html',
                           form=form, projects=lists)


@app.route('/project/<int:proj_id>', methods=['GET', 'POST'])
@login_required
def project_index(proj_id):
    # TODO: 삭제/수정하는 뷰 없음
    result = RequestProjectAPI.get_project_list()
    lists = result['items']

    return render_template('pages/project/list.html',
                           projects=lists)

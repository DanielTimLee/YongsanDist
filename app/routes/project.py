from flask import render_template, flash, redirect, url_for

from app import app
from app.forms.project import AddProjectForm, ModifyProjectForm
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
        if response_data['success']:
            flash('성공적으로 프로젝트를 추가했습니다.')
            return redirect(url_for('project_list'))

    elif form.is_submitted():
        flash('프로젝트 추가에 문제가 발생했습니다.')

    return render_template('pages/project/list.html',
                           form=form, projects=lists)


@app.route('/project/<int:project_id>', methods=['GET', 'POST'])
@login_required
def project_info(project_id):
    mod_form = ModifyProjectForm()
    project = RequestProjectAPI.get_project(project_id)

    if mod_form.validate_on_submit():
        payload = dict(
            title=mod_form.title.data,
            description=mod_form.description.data
        )
        response_data = RequestProjectAPI.mod_project(project_id, payload)
        if response_data['success']:
            flash('성공적으로 프로젝트를 수정했습니다.')
            return redirect(url_for('project_info', project_id=project_id))

    elif mod_form.is_submitted():
        flash('프로젝트 수정에 문제가 발생했습니다.')

    return render_template('pages/project/info.html',
                           form=mod_form, project=project)


# TODO: 세션 체커의 개념을 이용해서 한번 더 처리해주기
@app.route('/project/<int:project_id>/del')
@login_required
def project_del(project_id):
    response_data = RequestProjectAPI.del_project(project_id)
    if response_data['success']:
        flash('성공적으로 프로젝트를 수정했습니다.')

    else:
        flash('프로젝트 삭제에 문제가 발생했습니다.')

    return redirect(url_for('project_list'))

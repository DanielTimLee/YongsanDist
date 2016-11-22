import os

from flask import render_template, flash, redirect, url_for, request
from werkzeug.utils import secure_filename

from app import app
from app.forms.project import AddProjectForm, ModifyProjectForm, TargetUploadForm
from app.helpers.api_request import RequestProjectAPI, RequestTargetAPI, RequestAnalyzeAPI, RequestResultAPI
from app.helpers.target_process import csv_reader
from app.routes.oauth import login_required

# TODO: 나중에 tsv 파일도 import 가능하게.
ALLOWED_EXTENSIONS = set(['csv'])

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
def project_view(project_id):
    start = request.args.get('start')
    if start == str(1):
        response_data = RequestAnalyzeAPI.analyze_init(project_id)
        flash(response_data['messages'][0])
        return redirect(url_for('project_view', project_id=project_id))

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
            return redirect(url_for('project_view', project_id=project_id))

    elif mod_form.is_submitted():
        flash('프로젝트 수정에 문제가 발생했습니다.')

    return render_template('pages/project/view.html',
                           form=mod_form, project=project)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/project/<int:project_id>/target', methods=['GET', 'POST'])
@login_required
def target_index(project_id):
    try:
        dir = os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'])
        target_filename = '/' + str(project_id) + '.csv'
        target_file = csv_reader(dir + target_filename)

    except Exception:
        target_file = None

    done = request.args.get('done')
    if done == str(1):
        response_data = RequestTargetAPI.post_project_target(project_id, target_file.csv_dict)
        flash(response_data['messages'][0])
        return redirect(url_for('project_view', project_id=project_id))

    form = TargetUploadForm()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        if filename and allowed_file(filename):
            dir = os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'])
            if not os.path.exists(dir):
                os.makedirs(dir)

            new_filename = '/' + str(project_id) + '.csv'
            form.file.data.save(dir + new_filename)
            flash('파일 업로드에 성공했습니다.')
            return redirect(url_for('target_index', project_id=project_id))

    return render_template('pages/project/target/index.html',
                           targets=target_file,
                           project_id=project_id,
                           form=form)


# @login_required
@app.route('/project/<int:project_id>/result', methods=['GET', 'POST'])
def project_result(project_id):
    result = RequestResultAPI.get_result(project_id)
    print(result['project'])
    print(result['keyword'])
    print(result['demo_list'])
    print("hi")
    return "hi"

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

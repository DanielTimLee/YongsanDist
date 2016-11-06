from flask import render_template, redirect, url_for, flash

from app import app
from app.forms.document import DocumentForm
from app.helpers.api_request import RequestDocumentAPI
from app.routes.oauth import get_oauth_url


@app.route("/board/<board_name>")
def document_list(board_name):
    result = RequestDocumentAPI.get_list(board_name)

    return render_template('pages/document/list.html',
                           signin=get_oauth_url(),
                           board=board_name,
                           list=result['items'])


@app.route("/board/<board_name>/write", methods=['GET', 'POST'])
def document_add(board_name):
    form = DocumentForm()

    if form.validate_on_submit():
        response_data = RequestDocumentAPI.add_item(board_name,
                                                    form.title.data,
                                                    form.content.data)
        if response_data['success']:
            flash('성공적으로 게시글을 추가했습니다.')
            # TODO: project_list 수정
            return redirect(url_for('project_list'))

    elif form.is_submitted():
        flash('게시글 추가에 문제가 발생했습니다.')

    return render_template('pages/document/write.html',
                           signin=get_oauth_url(),
                           board=board_name,
                           form=form)


@app.route("/board/<board_name>/view/<document_id>")
def document_view(board_name, document_id):
    result = RequestDocumentAPI.get_item(document_id)

    return render_template('pages/document/view.html',
                           signin=get_oauth_url(),
                           board=board_name,
                           document=result)


@app.route("/board/<board_name>/modify/<document_id>")
def document_mod(board_name, document_id):
    form = DocumentForm()
    result = RequestDocumentAPI.get_item(document_id)
    form.title.data = result['title']
    form.content.data = result['content']

    if form.validate_on_submit():
        response_data = RequestDocumentAPI.add_item(board_name,
                                                    form.title.data,
                                                    form.content.data)
        if response_data['success']:
            flash('성공적으로 게시글을 추가했습니다.')
            return redirect(url_for('project_list'))

    elif form.is_submitted():
        flash('게시글 추가에 문제가 발생했습니다.')

    return render_template('pages/document/modify.html',
                           signin=get_oauth_url(),
                           board=board_name,
                           form=form)


@app.route("/board/<board_name>/delete/<document_id>")
def document_del(board_name, document_id):
    response_data = RequestDocumentAPI.del_item(document_id)
    flash(response_data['messages'][0])
    return redirect(url_for('document_list', board_name=board_name))

from flask import request, redirect, render_template, flash, url_for

from app import app, COOKIE_KEY_ACCESS_TOKEN, COOKIE_KEY_USER_DATA
from app.forms.user import ModifyProfileForm, VerifymeForm, ModifyPasswordForm
from app.helpers.api_request import RequestUserAPI, RequestVerifyUserAPI
from app.helpers.util import extract_username, Validation, extract_user_name, extract_user_email, extract_user_nickname, \
    extract_user_company
from app.routes.oauth import login_required


@app.route('/me/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('pages/user/dashboard.html')


@app.route("/me/signin_history")
@login_required
def signin_history():
    response_data, response_code = RequestUserAPI.get_signin_history_data()

    return render_template('pages/user/signin_history.html',
                           history=response_data)


@app.route("/me/verify", methods=['GET', 'POST'])
@login_required
def verify_me():
    form = VerifymeForm(request.form)
    form.username.data = extract_username(request.cookies)

    if Validation(form):
        payload = dict(password=form.password.data)

        response_data, response_code = RequestVerifyUserAPI.verify_password(payload)

        if not response_data['success']:
            return render_template('pages/user/verify_me.html',
                                   form=form,
                                   message={
                                       'error': {
                                           'title': '잘못된 입력입니다.',
                                           'contents': response_data['messages'][0]
                                       }
                                   })

        elif response_data['success']:
            return redirect(url_for('modify_profile'))

    return render_template('pages/user/verify_me.html',
                           form=form)


@app.route('/me/modify_profile', methods=['GET', 'POST'])
@login_required
def modify_profile():
    # TODO: Overwrite 해서 변경사향 적용 안됨 (너무 특정한 데이터를 선택해 넣음).
    form = ModifyProfileForm(request.form)
    if not form.username.data:
        form.username.data = extract_username(request.cookies)
        form.name.data = extract_user_name(request.cookies)
        form.nickname.data = extract_user_nickname(request.cookies)
        form.email.data = extract_user_email(request.cookies)
        form.company.data = extract_user_company(request.cookies)

    if Validation(form):
        payload = dict(name=form.name.data,
                       nickname=form.nickname.data,
                       email=form.email.data,
                       company=form.company.data)

        response_data, response_code = RequestUserAPI.mod_user_data(payload)
        flash(response_data['messages'][0])
        if not response_data['success']:
            return redirect(url_for('modify_profile'))

        # TODO: 회원정보 수정 후 cookie_bake ??
        return redirect(url_for('modify_profile'))

    return render_template('pages/user/modify_profile.html',
                           form=form)


@app.route('/me/modify_password', methods=['GET', 'POST'])
@login_required
def modify_password():
    form = ModifyPasswordForm(request.form)
    if Validation(form):
        payload = dict(password=form.password.data,
                       new_password=form.new_password.data)

        response_data, response_code = RequestUserAPI.mod_user_data(payload)
        flash(response_data['messages'][0])
        if not response_data['success']:
            return redirect(url_for('modify_password'))

        return redirect(url_for('index'))

    return render_template('pages/user/modify_password.html',
                           form=form)


@app.route("/signout")
@login_required
def signout():
    response = redirect(url_for('index'))
    response.set_cookie(COOKIE_KEY_ACCESS_TOKEN, expires=0)
    response.set_cookie(COOKIE_KEY_USER_DATA, expires=0)

    return response

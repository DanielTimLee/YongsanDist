from flask import render_template, url_for

from app import app


@app.errorhandler(500)
def internal_server_error(e):
    data = {
        'title': '500!!',
        'header': '다 저희 잘못입니다...',
        'message': '서버를 발로 짜서 죄송합니다! <br/> 죄송합니다! 죄송합니다! 죄송합니다!'
    }
    return render_template('pages/error/error.html', data=data), 500


@app.errorhandler(404)
def page_not_found(e):
    data = {
        'title': '404!!',
        'header': '여기가 어디죠?',
        'message': '죄송합니다. 요청하신 페이지를 찾을 수 없습니다. <br/> URL을 다시 한번 확인해주세요.'
    }
    return render_template('pages/error/error.html', data=data), 404


@app.errorhandler(400)
def bad(e):
    data = {
        'title': '400!!',
        'header': '잘못된 요청입니다!',
        'message': '뭔가 잘못된 요청인걸요?'
    }

    return render_template('pages/error/error.html', data=data), 400


@app.route('/error/permission', methods=['GET'])
def permission_denied():
    return render_template('error/permission.html',
                           auth_url=url_for('authentication'))

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Length, required, EqualTo
from wtforms_components import ModelForm


# TODO: 가능하면 FlaskForm으로 모두 바꿔줄 수 있게.
class ModifyProfileForm(ModelForm):
    username = StringField('ID', [])
    password = PasswordField('Password', [])
    confirm_password = PasswordField('Confirm Password', [])
    name = StringField('Name', [])
    nickname = StringField('Nickname', [])
    email = EmailField('Email', [])


class ModifyPasswordForm(ModelForm):
    password = PasswordField('Password', [
        required(message='비밀번호는 필수 항목입니다.'),
        Length(min=6, max=20, message='%(min)d 이상 %(max)d 이하로 입력해주세요.')
    ])
    new_password = PasswordField('New Password', [
        required(message='비밀번호는 필수 항목입니다.'),
        Length(min=6, max=20, message='%(min)d 이상 %(max)d 이하로 입력해주세요.')
    ])
    new_confirm_password = PasswordField('New Confirm Password', [
        required(message='비밀번호 확인값은 필수 항목입니다.'),
        EqualTo('password', message='비밀번호와 비밀번호 확인값이 일치하지 않습니다.')
    ])


class VerifymeForm(FlaskForm):
    username = StringField('ID', [
        required(message='비밀번호는 필수 항목입니다.'),
        Length(min=4, max=15, message='%(min)d 이상 %(max)d 이하로 입력해주세요.')
    ])
    password = PasswordField('Password', [
        required(message='비밀번호는 필수 항목입니다.'),
        Length(min=6, max=20, message='%(min)d 이상 %(max)d 이하로 입력해주세요.')
    ])

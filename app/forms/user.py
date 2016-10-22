from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Length, required, EqualTo
from wtforms_components import Email, ModelForm


# TODO: 가능하면 FlaskForm으로 모두 바꿔줄 수 있게.
class ModifyProfileForm(ModelForm):
    username = StringField('ID', [
        required(message='ID는 필수 항목입니다.'),
        Length(min=4, max=20, message='%(min)d글자 이상 %(max)d글자 이하로 입력해주세요.')
    ])
    password = PasswordField('Password', [])
    # confirm_password = PasswordField('Confirm Password', [])
    name = StringField('Name', [
        required(message='이름은 필수 항목입니다.'),
        Length(min=2, max=10, message='%(min)d 이상 %(max)d 이하로 입력해주세요.')
    ])
    nickname = StringField('Nickname', [
        required(message='닉네임은 필수 항목입니다.'),
        Length(min=4, max=16)
    ])
    email = EmailField('Email', [
        required(message='이메일은 필수 항목입니다.'),
        Email(message='유효한 이메일 주소를 입력해주세요.')
    ])
    company = StringField('Company', [
        required(message='소속은 필수 항목입니다.'),
        Length(min=2, max=20, message='%(min)d 이상 %(max)d 이하로 입력해주세요.')
    ])


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

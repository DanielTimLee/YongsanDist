from wtforms import StringField, PasswordField, Form
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, required, EqualTo
from wtforms_components import ModelForm


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


class VerifymeForm(Form):
    username = StringField('ID', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])

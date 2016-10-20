from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length, required, DataRequired


class AddProjectForm(FlaskForm):
    title = StringField('Title', [
        DataRequired(message='프로젝트 이름은 필수 항목입니다'),
        Length(min=4, max=100, message='%(min)d 이상 %(max)d 이하로 입력해주세요.')
    ])
    description = StringField('Description', [
        DataRequired(message='프로젝트 설명은 필수 항목입니다.'),
        Length(min=4, max=255, message='%(min)d 이상 %(max)d 이하로 입력해주세요.')
    ])


class ModifyProjectForm(FlaskForm):
    title = StringField('Title', [
        required(message='프로젝트 이름은 필수 항목입니다'),
        Length(min=4, max=100, message='%(min)d 이상 %(max)d 이하로 입력해주세요.')
    ])
    description = StringField('Description', [
        required(message='프로젝트 설명은 필수 항목입니다.'),
        Length(min=4, max=255, message='%(min)d 이상 %(max)d 이하로 입력해주세요.')
    ])


# TODO: 깃헙처럼 Delete Form
class DeleteProjectForm(FlaskForm):
    title = StringField('Title', [
        required(message='프로젝트 이름을 다시 한번 입력해 주세요'),
        Length(min=4, max=100, message='%(min)d 이상 %(max)d 이하로 입력해주세요.')
    ])

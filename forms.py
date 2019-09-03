# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required

class NameForm(FlaskForm):
    name = StringField('名字', validators=[Required()])
    pwd = PasswordField('密码', validators=[Required()])
    submit = SubmitField('提交')

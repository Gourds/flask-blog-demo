# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import Required,Length,Email

class NameForm(FlaskForm):
    name = StringField('名字', validators=[Required()])
    pwd = PasswordField('密码', validators=[Required()])
    submit = SubmitField('提交')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1,64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('Log In')
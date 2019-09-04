# -*- coding:utf-8 -*-

class base_config():
    SECRET_KEY = 'helloworld'

class development(base_config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/data.sqlite'
    #sqlite:后面跟的3个斜杠表示相对路径，四个斜杠则表示是绝对路径
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Gourds]'
    FLASK_MAIL_SENDER = '<gourds@tom.com>'
    MAIL_SERVER = ''
    MAIL_PORT = None
    MAIL_USE_TLS = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
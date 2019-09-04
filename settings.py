# -*- coding:utf-8 -*-

class base_config():
    SECRET_KEY = 'helloworld'

class development(base_config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + './data.sqlite'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Gourds]'
    FLASK_MAIL_SENDER = '<gourds@tom.com>'
    MAIL_SERVER = ''
    MAIL_PORT = None
    MAIL_USE_TLS = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
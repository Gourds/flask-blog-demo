# -*- coding:utf-8 -*-
from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('settings.development')
Bootstrap(app)
Moment(app)

from app.views import user
from app.views import index
from app.views import login

app.register_blueprint(user.mod, url_prefix='/v1')
app.register_blueprint(index.mod, url_prefix='/v1')
app.register_blueprint(login.mod, url_prefix='/v1')

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login.mod'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html'),500


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')
    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    def __repr__(self):
        return '<User %r>' % self.username


db.create_all()



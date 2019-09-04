# -*- coding:utf-8 -*-
from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment

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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html'),500





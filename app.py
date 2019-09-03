# -*- coding:utf-8 -*-

from flask import Flask,render_template,flash
from flask import request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from forms import NameForm
from flask_mail import Message,Mail
# from flask_script import Shell,Manager
# from flask_migrate import Migrate, MigrateCommand
from sql import Role,User

app = Flask(__name__)
app.config.from_object('settings.development')
Bootstrap(app)
Moment(app)
mail = Mail(app)
db = SQLAlchemy(app)
# manager = Manager(app)
# def make_shell_context():
#     return dict(app=app, db=db, User=User, Role=Role)
# manager.add_command('shell', Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASK_MAIL_SENDER'],recipients=[to]
                  )
    # msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)

@app.route('/login', methods=['GET','POST'])
def login():
    form = NameForm()
    print(form.name)
    print(form.pwd)
    flash('success login')
    send_email(to='gourds@tom.com',subject='TM', template='user')
    return render_template('login.html', form=form)

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/index')
def index():
    return render_template('index.html',current_time=datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('404.html'),500


if __name__ == '__main__':
    app.run()
    # manager.run()
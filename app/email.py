# -*- coding:utf-8 -*-
# from flask_mail import Message,Mail
#
# app = Flask(__name__)
# mail = Mail(app)
#
# def send_email(to, subject, template, **kwargs):
#     msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
#                   sender=app.config['FLASK_MAIL_SENDER'],recipients=[to]
#                   )
#     # msg.body = render_template(template + '.txt', **kwargs)
#     msg.html = render_template(template + '.html', **kwargs)
#     mail.send(msg)
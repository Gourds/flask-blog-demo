
from flask import Blueprint,render_template,flash,request,redirect,url_for
from app.views.forms import NameForm,LoginForm
from flask_login import UserMixin,user_unauthorized

mod = Blueprint('login',__name__)


@mod.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('auth.html',form=form)
    flash('success login')
    print(request.form)
    return redirect(url_for('index.index'))
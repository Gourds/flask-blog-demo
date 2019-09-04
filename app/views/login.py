
from flask import Blueprint,render_template,flash
from app.views.forms import NameForm

mod = Blueprint('login',__name__)


@mod.route('/login', methods=['GET','POST'])
def login():
    form = NameForm()
    print(form.name)
    print(form.pwd)
    flash('success login')
    return render_template('login.html', form=form)